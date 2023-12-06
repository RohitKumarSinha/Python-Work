from flask import Flask, render_template, request
import boto3
from werkzeug.utils import secure_filename
# import os
# import uuid

# from flask_s3 import FlaskS3

app = Flask(__name__)

s3 = boto3.client('s3',aws_access_key_id='AKIARJYW7PAEB6TJWUWC',aws_secret_access_key='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')

BUCKET_NAME='datavisualizationn'

@app.route('/')
def hello_world():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "

    return render_template("file_upload_to_s3.html",msg =msg)

@app.route('/data')
def display_data():
    response = s3.get_object(Bucket='write-visualizedata', Key='write-data/my-data-transformed.csv/part-00000-a759ad7a-2cef-4cdf-ac31-bf36d83999ce-c000.csv')
    data = response['Body'].read().decode('utf-8')
    return render_template('data.html', data=data)

# app.config['S3_BUCKET_NAME'] = 'datavisualizationn'
# app.config['AWS_ACCESS_KEY_ID'] = 'AKIARJYW7PAEB6TJWUWC'
# app.config['AWS_SECRET_ACCESS_KEY'] = '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'

# s3 = FlaskS3(app)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['file']
#     file_name = str(uuid.uuid4()) + '.csv'
#     s3.upload_file(file, app.config['S3_BUCKET_NAME'], file_name)
#     return 'File uploaded successfully!'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)

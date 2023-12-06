import pandas as pd
from tabulate import tabulate

import psycopg2

# PostgreSQL database connection details
db_host = 'postgres-database.cuf9bbt9ukt6.ap-south-1.rds.amazonaws.com'
db_port = '5432'
db_name = 'db_test'
db_user = 'postgres'
db_password = 'postgres'

# Create an empty dictionary to store the data
data = {}

# Assuming you have a list of tab names in your Excel file
tab_names = ['Sec-1_Exp_LargeBorr', 'Sec-2_WriteOff', 'Sec-3_CurrAc', 'Sec-4_NonCo-op Borr']

# Specify the CSV file paths and corresponding row and column ranges
csv_files = {
    'General Information': {
        'file_path': '/content/General_Information.csv',
        'start_row': 9,
        'end_row': 19,
        'start_col': 4,
        'end_col': 5
    },
    'Authorised': {
        'file_path': '/content/Authorised_Signatory.csv',
        'start_row': 10,
        'end_row': 13,
        'start_col': 4,
        'end_col': 5
    }
}

# Iterate over each CSV file
for tab_name, file_info in csv_files.items():
    # Read the CSV file
    csv_file = pd.read_csv(file_info['file_path'])

    # Slice the DataFrame based on the specified row and column range
    df = csv_file.iloc[
        file_info['start_row']-1 : file_info['end_row'],
        file_info['start_col']-1 : file_info['end_col']
    ]

    # Store the DataFrame in the dictionary with the tab name as the key
    data[tab_name] = df

# Iterate over each tab
for tab_name in tab_names:
    if tab_name == 'Sec-1_Exp_LargeBorr':
        start_row = 32
        end_row = 39
        start_col = 3
        end_col = 78
    elif tab_name == 'Sec-2_WriteOff':
        start_row = 22
        end_row = 27
        start_col = 3
        end_col = 18
    elif tab_name == 'Sec-3_CurrAc':
        start_row = 22
        end_row = 29
        start_col = 3
        end_col = 10
    elif tab_name == 'Sec-4_onCo-op Borr':
        start_row = 9
        end_row = 14
        start_col = 3
        end_col = 10

    # Read the Excel file and extract the desired data range
    df = pd.read_excel('/content/CRILC_1303202385ABA38B7B6349509E723824B0F07306.XLSX', sheet_name=tab_name, header=None, skiprows=start_row-1, nrows=(end_row - start_row + 1), usecols=lambda x: start_col <= x <= end_col)

    # Store the DataFrame in the dictionary with the tab name as the key
    data[tab_name] = df

# Database connection
conn = psycopg2.connect(host=db_host, port=db_port, database=db_name, user=db_user, password=db_password)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Iterate over the data dictionary
for tab_name, df in data.items():
    # Remove spaces from the tab name and replace hyphens with underscores
    table_name = tab_name.replace(" ", "").replace("-", "_")

    # Create a new table with the modified name
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

    # Generate the column names and data types for the table
    column_names = []
    for col in df.columns:
        # Convert column name to lowercase and remove spaces, hyphens, and invalid characters
        col_name = str(col).lower().replace(" ", "_").replace("-", "").replace(":", "")
        column_names.append(col_name)
        create_table_query += f'"{col_name}" VARCHAR(255), '

    create_table_query = create_table_query.rstrip(', ') + ")"
    cursor.execute(create_table_query)

    # Insert the data into the table
    for row in df.itertuples(index=False):
        # Filter out missing values (NaN)
        values = [value if pd.notna(value) else None for value in row]

        # Generate the list of placeholders
        placeholders = ', '.join(['%s' for _ in column_names])

        # Lowercase the column names in the INSERT query and enclose them in double quotes
        insert_query = "INSERT INTO " + table_name + " (" + ', '.join(['"' + col + '"' for col in column_names]) + ") VALUES (" + placeholders + ")"
        cursor.execute(insert_query, values)

# Commit the changes
conn.commit()







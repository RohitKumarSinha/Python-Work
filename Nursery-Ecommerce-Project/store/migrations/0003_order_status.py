# Generated by Django 3.1 on 2020-08-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
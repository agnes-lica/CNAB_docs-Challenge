# Generated by Django 4.1.5 on 2023-01-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_transaction_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_description',
            field=models.CharField(default='1', max_length=61),
        ),
    ]

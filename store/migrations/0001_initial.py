# Generated by Django 4.1.5 on 2023-01-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=14, unique=True)),
                ('owner', models.CharField(max_length=19)),
            ],
        ),
    ]

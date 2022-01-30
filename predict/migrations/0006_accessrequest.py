# Generated by Django 4.0.1 on 2022-01-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0005_datafile_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=300)),
                ('representativeName', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
    ]

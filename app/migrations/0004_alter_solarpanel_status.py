# Generated by Django 4.2.8 on 2024-01-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_solarpanel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=10),
        ),
    ]

# Generated by Django 4.2.8 on 2024-01-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_maintainance'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarpanel',
            name='status',
            field=models.CharField(default=1, max_length=10, verbose_name=(('Active', 'Active'), ('Inactive', 'Inactive'))),
            preserve_default=False,
        ),
    ]

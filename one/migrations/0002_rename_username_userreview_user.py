# Generated by Django 5.0.2 on 2024-08-01 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreview',
            old_name='Username',
            new_name='User',
        ),
    ]
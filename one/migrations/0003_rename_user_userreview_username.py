# Generated by Django 5.0.2 on 2024-08-01 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_rename_username_userreview_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreview',
            old_name='User',
            new_name='Username',
        ),
    ]

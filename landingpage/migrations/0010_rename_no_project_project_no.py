# Generated by Django 3.2.9 on 2022-07-11 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0009_project_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='no',
            new_name='Project_no',
        ),
    ]
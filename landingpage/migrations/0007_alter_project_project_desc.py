# Generated by Django 3.2.9 on 2021-12-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0006_auto_20211129_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Project_desc',
            field=models.TextField(max_length=3500),
        ),
    ]

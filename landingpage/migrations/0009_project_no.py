# Generated by Django 3.2.9 on 2022-07-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0008_project_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='no',
            field=models.TextField(default='SOME STRING', max_length=140),
        ),
    ]

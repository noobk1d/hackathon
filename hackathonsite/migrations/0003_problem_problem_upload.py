# Generated by Django 3.2 on 2021-04-23 11:30

from django.db import migrations, models
import hackathonsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonsite', '0002_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_upload',
            field=models.FileField(blank=True, default='', upload_to=hackathonsite.models.user_directory_path),
        ),
    ]
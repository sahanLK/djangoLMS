# Generated by Django 4.1.7 on 2023-04-07 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0019_question_meeting_recording_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='time_start',
            new_name='start',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 7, 22, 32, 38, 330940)),
        ),
    ]

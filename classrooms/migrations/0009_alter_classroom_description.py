# Generated by Django 4.1.7 on 2023-03-31 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0008_alter_classroom_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]

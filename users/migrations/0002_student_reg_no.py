# Generated by Django 4.1.7 on 2023-05-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='reg_no',
            field=models.CharField(default='', max_length=13),
        ),
    ]

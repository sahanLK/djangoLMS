# Generated by Django 4.1.7 on 2023-03-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0005_alter_lecturer_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='department',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='departments',
            field=models.ManyToManyField(blank=True, to='main.department'),
        ),
    ]

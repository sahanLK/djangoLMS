# Generated by Django 4.1.7 on 2023-04-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0013_assignment_review_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
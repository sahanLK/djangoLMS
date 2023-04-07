# Generated by Django 4.1.7 on 2023-04-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_delete_adminmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='lec_profile_pics'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_pic',
            field=models.ImageField(blank=True, null=True, upload_to='stu_id_pics'),
        ),
    ]

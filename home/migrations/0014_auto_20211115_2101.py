# Generated by Django 3.1.8 on 2021-11-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_edit_profile_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_profile_model',
            name='cv',
            field=models.FileField(upload_to='cv/'),
        ),
        migrations.AlterField(
            model_name='edit_profile_model',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_picture/'),
        ),
    ]

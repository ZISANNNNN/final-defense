# Generated by Django 3.1.8 on 2021-11-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211115_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='edit_profile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('previous_job', models.CharField(max_length=1000, null=True)),
                ('your_field_of_job', models.CharField(max_length=1000)),
                ('profile_picture', models.FileField(upload_to='')),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
    ]

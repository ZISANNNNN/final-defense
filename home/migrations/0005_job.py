# Generated by Django 3.1.8 on 2021-10-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('jobs', models.CharField(max_length=1000)),
            ],
        ),
    ]

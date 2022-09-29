# Generated by Django 3.1.8 on 2021-10-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211028_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('jobs', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='cv',
        ),
        migrations.DeleteModel(
            name='resume',
        ),
    ]

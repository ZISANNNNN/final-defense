# Generated by Django 3.1.8 on 2022-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20220112_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_for_job',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apply_for_job',
            name='post_id',
            field=models.IntegerField(max_length=1000),
        ),
    ]

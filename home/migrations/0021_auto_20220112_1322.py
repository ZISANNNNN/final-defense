# Generated by Django 3.1.8 on 2022-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20220112_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_for_job',
            name='email',
            field=models.IntegerField(null=True),
        ),
    ]

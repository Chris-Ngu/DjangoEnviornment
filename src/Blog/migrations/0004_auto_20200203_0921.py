# Generated by Django 3.0.2 on 2020-02-03 15:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20200202_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 15, 21, 26, 788058, tzinfo=utc)),
        ),
    ]

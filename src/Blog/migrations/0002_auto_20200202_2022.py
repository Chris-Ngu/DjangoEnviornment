# Generated by Django 3.0.2 on 2020-02-03 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='active',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 2, 20, 22, 8, 808689)),
        ),
    ]

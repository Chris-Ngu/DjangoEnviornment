# Generated by Django 3.0.2 on 2020-01-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='This is cool'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-09-17 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myDoctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='last_name',
        ),
    ]

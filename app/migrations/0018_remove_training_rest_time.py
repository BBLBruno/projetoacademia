# Generated by Django 5.1.3 on 2025-01-18 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_trainingsheet_name_training_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='rest_time',
        ),
    ]

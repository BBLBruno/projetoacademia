# Generated by Django 5.1.3 on 2025-01-18 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_exercise_rest_time_remove_training_exercises_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='ficha_de_treino',
        ),
    ]

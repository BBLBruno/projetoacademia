# Generated by Django 5.1.3 on 2025-01-18 03:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_exercise_rest_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='exercises',
        ),
        migrations.CreateModel(
            name='TrainingExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1, verbose_name='Ordem')),
                ('sets', models.IntegerField(default=3, verbose_name='Número de Séries')),
                ('repetitions', models.IntegerField(default=12, verbose_name='Número de Repetições')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.exercise', verbose_name='Exercício')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.training', verbose_name='Treino')),
            ],
        ),
    ]

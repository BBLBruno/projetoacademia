# Generated by Django 5.1.3 on 2025-01-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_training_rest_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsheet',
            name='series',
            field=models.IntegerField(default=12, verbose_name='Número de Séries'),
        ),
    ]

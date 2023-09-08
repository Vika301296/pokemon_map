# Generated by Django 4.2.5 on 2023-09-08 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 8, 20, 34, 29, 679522)
            ),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 8, 20, 34, 29, 679533)
            ),
        ),
    ]

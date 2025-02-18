# Generated by Django 4.2.5 on 2023-09-08 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0002_pokemonentity_appeared_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonentity",
            name="defence",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="health",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="level",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="stamina",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="strength",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 8, 20, 38, 4, 604975)
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 8, 20, 38, 4, 604985)
            ),
        ),
    ]

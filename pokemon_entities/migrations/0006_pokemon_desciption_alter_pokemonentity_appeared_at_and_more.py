# Generated by Django 4.2.5 on 2023-09-09 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0005_alter_pokemonentity_appeared_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="desciption",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 9, 7, 17, 56, 574528)
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 9, 7, 17, 56, 574538)
            ),
        ),
    ]

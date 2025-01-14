# Generated by Django 4.2.5 on 2023-09-09 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "pokemon_entities",
            "0006_pokemon_desciption_alter_pokemonentity_appeared_at_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="title_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pokemon",
            name="title_jp",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 9, 7, 28, 56, 242884)
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 9, 7, 28, 56, 242894)
            ),
        ),
    ]

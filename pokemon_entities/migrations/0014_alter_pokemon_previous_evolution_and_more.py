# Generated by Django 4.2.5 on 2023-09-16 23:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "pokemon_entities",
            "0013_alter_pokemon_desciption_alter_pokemon_title_en_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="previous_evolution",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="next_evolutions",
                to="pokemon_entities.pokemon",
                verbose_name="Из кого эволюционировал",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 16, 23, 1, 55, 192906),
                verbose_name="Когда появился",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 16, 23, 1, 55, 192918),
                verbose_name="Когда исчез",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pokemon",
                to="pokemon_entities.pokemon",
                verbose_name="Покемон",
            ),
        ),
    ]

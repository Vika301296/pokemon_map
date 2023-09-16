# Generated by Django 4.2.5 on 2023-09-10 18:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0010_remove_pokemon_next_evolution_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="previous_evolution",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="next_evolution",
                to="pokemon_entities.pokemon",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 10, 18, 51, 11, 932903)
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 10, 18, 51, 11, 932913)
            ),
        ),
    ]
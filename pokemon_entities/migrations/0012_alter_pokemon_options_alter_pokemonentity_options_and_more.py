# Generated by Django 4.2.5 on 2023-09-16 22:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0011_alter_pokemon_previous_evolution_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pokemon",
            options={"verbose_name": "Покемон", "verbose_name_plural": "Покемоны"},
        ),
        migrations.AlterModelOptions(
            name="pokemonentity",
            options={
                "verbose_name": "Экземпляр покемонов",
                "verbose_name_plural": "Экземпляры покемонов",
            },
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="desciption",
            field=models.TextField(
                blank=True, max_length=1000, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="pokemons", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="previous_evolution",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="next_evolution",
                to="pokemon_entities.pokemon",
                verbose_name="Из кого эволюционировал",
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title_en",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Название на английском",
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title_jp",
            field=models.TextField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Название на японском",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 16, 22, 48, 41, 226351),
                verbose_name="Когда появился",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="defence",
            field=models.IntegerField(blank=True, null=True, verbose_name="Защита"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 16, 22, 48, 41, 226361),
                verbose_name="Когда исчез",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="health",
            field=models.IntegerField(blank=True, null=True, verbose_name="Здоровье"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="lat",
            field=models.FloatField(blank=True, null=True, verbose_name="Ширина"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="level",
            field=models.IntegerField(blank=True, null=True, verbose_name="Уровень"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="lon",
            field=models.FloatField(blank=True, null=True, verbose_name="Долгота"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="pokemon",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pokemon",
                to="pokemon_entities.pokemon",
                verbose_name="Покемон",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="stamina",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Выносливаость"
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="strength",
            field=models.IntegerField(blank=True, null=True, verbose_name="Сила"),
        ),
    ]

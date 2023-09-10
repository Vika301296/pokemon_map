import datetime

from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='pokemons')
    desciption = models.CharField(null=True, blank=True, max_length=1000)
    title_en = models.CharField(null=True, blank=True, max_length=50)
    title_jp = models.TextField(null=True, blank=True, max_length=50)
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='next_evolution')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, default=1, related_name='pokemon')
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    appeared_at = models.DateTimeField(default=datetime.datetime.now())
    disappeared_at = models.DateTimeField(default=datetime.datetime.now())
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.pokemon.title

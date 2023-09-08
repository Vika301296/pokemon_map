import datetime

from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='pokemons')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=datetime.datetime.now())
    disappeared_at = models.DateTimeField(default=datetime.datetime.now())

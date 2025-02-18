from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(
        null=True, blank=True, upload_to='pokemons',
        verbose_name='Изображение')
    desciption = models.TextField(
        blank=True, max_length=1000, verbose_name='Описание')
    title_en = models.CharField(
        blank=True, max_length=50,
        verbose_name='Название на английском',)
    title_jp = models.TextField(blank=True, max_length=50,
                                verbose_name='Название на японском',)
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='next_evolutions',
        verbose_name='Из кого эволюционировал')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        related_name='entities', verbose_name='Покемон')
    lat = models.FloatField(null=True, blank=True, verbose_name='Ширина')
    lon = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        verbose_name='Когда появился')
    disappeared_at = models.DateTimeField(verbose_name='Когда исчез')
    level = models.IntegerField(null=True, blank=True,
                                verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True,
                                 verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True,
                                   verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True,
                                  verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True,
                                  verbose_name='Выносливаость')

    def __str__(self):
        return self.pokemon.title

    class Meta:
        verbose_name = 'Экземпляр покемонов'
        verbose_name_plural = 'Экземпляры покемонов'

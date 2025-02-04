from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название на русском')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название на японском')
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey('self', related_name='next_evolution', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Предыдущая эволюция')

    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='entities', on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта', blank=True, null=True)
    lon = models.FloatField(verbose_name='Долгота', blank=True, null=True)
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Появился в')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Исчез в')
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defense = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title_ru} (Lat: {self.lat}, Lon: {self.lon}, Level: {self.level})'

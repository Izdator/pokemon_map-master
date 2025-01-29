from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)
    description = models.CharField(max_length=500)

    evolution = models.ForeignKey(
        'self',
        related_name='next_evolution',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    previous_evolution = models.ForeignKey(
        'self',
        related_name='previous_evolution_pokemon',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='entities', on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    strength = models.IntegerField(default=10)
    defense = models.IntegerField(default=10)
    stamina = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.pokemon.title_ru} (Lat: {self.lat}, Lon: {self.lon}, Level: {self.level})'

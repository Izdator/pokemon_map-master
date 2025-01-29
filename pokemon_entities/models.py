from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='entities', on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    Level = models.IntegerField(default=1)
    Health = models.IntegerField(default=100)
    Strength = models.IntegerField(default=10)
    Defense = models.IntegerField(default=10)
    Stamina = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.pokemon.title} (Lat: {self.lat}, Lon: {self.lon}, Level: {self.Level})'

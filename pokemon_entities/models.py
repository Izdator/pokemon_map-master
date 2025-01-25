from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='entities', on_delete=models.CASCADE) # Связь с моделью Pokemon
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f'{self.pokemon.title} (Lat: {self.lat}, Lon: {self.lon})'

from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

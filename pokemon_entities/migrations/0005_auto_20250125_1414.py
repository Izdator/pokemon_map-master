# Generated by Django 3.1.14 on 2025-01-25 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='longitude',
            new_name='lon',
        ),
    ]

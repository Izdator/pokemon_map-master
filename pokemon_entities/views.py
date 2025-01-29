import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    local_time = timezone.localtime()

    pokemons = Pokemon.objects.prefetch_related('entities').all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_on_page = []

    for pokemon in pokemons:
        for pokemon_entity in pokemon.entities.all():
            if pokemon_entity.appeared_at is not None and pokemon_entity.disappeared_at is not None:
                if pokemon_entity.appeared_at <= local_time < pokemon_entity.disappeared_at:
                    image_url = pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL
                    absolute_image_url = request.build_absolute_uri(image_url)
                    add_pokemon(
                        folium_map, pokemon_entity.lat,
                        pokemon_entity.lon,
                        absolute_image_url
                    )

                    pokemons_on_page.append({
                        'pokemon_id': pokemon.id,
                        'img_url': absolute_image_url,
                        'title_ru': pokemon.title,
                    })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon.objects.prefetch_related('entities'), id=pokemon_id)

    requested_pokemon = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL,
        'title_ru': pokemon.title,
        'entities': [],
        'description': pokemon.description
    }

    for pokemon_entity in pokemon.entities.all():
        requested_pokemon['entities'].append({
            'lat': pokemon_entity.lat,
            'lon': pokemon_entity.lon
        })

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon['entities']:
        add_pokemon(
            folium_map, pokemon_entity['lat'],
            pokemon_entity['lon'],
            requested_pokemon['img_url']
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': requested_pokemon
    })

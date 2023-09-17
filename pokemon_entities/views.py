import folium

from django.utils import timezone
from django.shortcuts import get_object_or_404, render

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
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_on_page = []
    current_time = timezone.now()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lt=current_time, disappeared_at__gt=current_time)
    for pokemon in pokemon_entities:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.pokemon.image.url),
            'title_ru': pokemon.pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon = {
        'img_url': request.build_absolute_uri(
            requested_pokemon.image.url),
        'title_ru': requested_pokemon.title,
        'description': requested_pokemon.desciption,
        'title_jp': requested_pokemon.title_jp,
        'title_en': requested_pokemon.title_en
    }
    if requested_pokemon.previous_evolution:
        pokemon['previous_evolution'] = {
            'title_ru': requested_pokemon.previous_evolution.title,
            'pokemon_id': requested_pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(
                requested_pokemon.previous_evolution.image.url),
        }
    next_evolution = requested_pokemon.next_evolutions.first()
    if next_evolution is not None:
        pokemon['next_evolution'] = {
            'title_ru': next_evolution.title,
            'pokemon_id': next_evolution.id,
            'img_url': request.build_absolute_uri(
                next_evolution.image.url),
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })

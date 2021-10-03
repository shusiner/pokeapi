# This file is to interact with with pokeapi.co

# region kanto
# https://pokeapi.co/api/v2/region/{id or name}/

# encounter method
# https://pokeapi.co/api/v2/encounter-method/{id or name}/

# location has many locations areas
# locations areas has many pokemon encounters
# https://pokeapi.co/api/v2/pokemon/{id or name}/encounters

# stats
# https://pokeapi.co/api/v2/pokemon/{id or name}

from datetime import datetime

import requests
import json

from pokemon import Pokemon
from exception import PokemonNotFoundError, ServerError
from interact_db import *
import csv

loaded_db = load_db()
location_areas_cached, pokemon_cached = set(loaded_db[0]), loaded_db[1]
pokemon_pair, pokemon_cached_ids = {}, {}
for i in pokemon_cached:
    pokemon_pair[i['name']] = i['id']
for i in pokemon_cached:
    pokemon_cached_ids[i['id']] = i
# overall
# return pokemon id, name, types, encounter locations and methods in kanto and stats

# get all locations and then area locations in kanto


def get_area_locations_in_kanto() -> list:
    response = requests.get('https://pokeapi.co/api/v2/region/1/')

    # maybe we can refactor this and check all methods that uses requests
    if response.status_code != 200:
        raise ServerError

    location_areas = []
    locations = json.loads(response.content.decode('utf-8'))['locations']
    for i in locations:
        response = requests.get(i['url'])
        areas = json.loads(response.content.decode('utf-8'))['areas']
        location_areas += [i['name'] for i in areas]

    return location_areas


def search_api(id_or_name: str) -> dict:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id_or_name}')
    if response.status_code == 404:
        raise PokemonNotFoundError(id_or_name)
    if response.status_code != 200:
        raise ServerError
    poke = json.loads(response.content.decode('utf-8'))
    poke_result = {}
    poke_result['id'] = poke['id']
    poke_result['name'] = poke['name']

    response = requests.get(
        f'https://pokeapi.co/api/v2/pokemon/{id_or_name}/encounters')
    encounters = json.loads(response.content.decode('utf-8'))
    location_areas = [(i['location_area']['name'], i['version_details'])
                      for i in encounters]
    location_areas_in_kanto = [
        i for i in location_areas if i[0] in location_areas_cached]
    poke_result['encounter_locations'] = [i[0]
                                          for i in location_areas_in_kanto]

    # not working, need to check
    # encounter_methods = [k['method']['name'] for k in
    # [j['encounter_details'] for j in [i[1] for i in location_areas_in_kanto]]]

    encounter_methods = []
    for i in location_areas_in_kanto:
        for j in i[1]:
            for k in j['encounter_details']:
                encounter_methods.append(k['method']['name'])

    unique_methods = list(set(encounter_methods))
    unique_methods.sort()
    poke_result['methods'] = unique_methods

    poke_result['stats'] = dict(
        [(i['stat']['name'], i['base_stat']) for i in poke['stats']])

    poke_result['datetime_searched'] = now = datetime.now().strftime(
        '%d/%m/%Y %H:%M:%S')

    if not poke_result.get(poke_result['id'], None):
        pokemon_cached.append(poke_result)
        pokemon_pair[poke_result['name']] = poke_result['id']
        pokemon_cached_ids[poke_result['id']] = poke_result
        update_db(pokemon_cached)
    return poke_result

# Need to take note of the time stored
# need to fetch from server when time of record expired, 1 week


def search_db_or_api(id_or_name: str) -> dict:
    fetch_from_server = False
    if id_or_name.isnumeric():
        poke = pokemon_cached_ids.get(int(id_or_name), None)
        if poke:
            pre_time = datetime.strptime(
                poke['datetime_searched'], '%d/%m/%Y %H:%M:%S')
            if (datetime.now() - pre_time).days > 7:
                fetch_from_server = True
        else:
            fetch_from_server = True
    else:
        poke_id = pokemon_pair.get(id_or_name, None)
        if poke_id:
            poke = pokemon_cached_ids[poke_id]
        else:
            fetch_from_server = True
    if fetch_from_server:
        poke = search_api(id_or_name)
    # print(fetch_from_server)
    return poke


def export_to_area_locations_db() -> bool:
    area_locations = get_area_locations_in_kanto()
    with open("location_areas.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows([[i] for i in area_locations])
    return True

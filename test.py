# This file is to test all the functions

import unittest
from interact_api import *
from pokemon import *
import requests
import json
from exception import PokemonNotFoundError
import csv

test_url1 = "https://pokeapi.co/api/v2/pokemon/2522"
result_25 = '{"id": 25, "name": "pikachu", "encounter_locations": ["pallet-town-area", "kanto-route-2-south-towards-viridian-city", "viridian-forest-area", "power-plant-area"], "methods": ["gift", "walk"], "stats": {"hp": 35, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "speed": 90}}'
result_25_dict = json.loads(result_25)


class TestInteractApi(unittest.TestCase):

    def test_pokemon_not_found_exception(self):
        self.assertRaises(PokemonNotFoundError, search_api, 2222)

    def test_pokemon_25_found(self):
        # print(search_api(25))
        self.assertEqual(isinstance(search_api(25),dict),True)

    def test_pokemon_26_found(self):
        self.assertEqual(isinstance(search_api(26),dict),True)

    def test_pokemon_26_found_db(self):
        self.assertEqual(isinstance(search_db_or_api("26"),dict),True)
        


class TestInteractDb(unittest.TestCase):

    def test_area_locations_length_csv(self):
        with open('location_areas.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(len(data), 145)

    # this test takes some time
    # def test_area_locations_length(self):
    #     self.assertEqual(len(get_area_locations_in_kanto()),145)

    # this is to get all area_locations from server
    # def test_export_to_area_locations_db(self):
    #     self.assertEqual(export_to_area_locations_db(),True)


class TestSample(unittest.TestCase):

    pass
    # def test_list_to_csv(self):
    #     with open("out.csv", "w", newline="") as f:
    #         writer = csv.writer(f)
    #         writer.writerows([["a"], ["b"]])

    # with open('out.json', 'w') as f:
    #     json.dump([result_25_dict],f)

    # with open('out.json') as f:
    #     g = json.load(f)
    #     print(g)



if __name__ == '__main__':
    unittest.main()

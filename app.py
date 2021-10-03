from exception import PokemonNotFoundError
from interact_api import search_db_or_api

first_load = True

instruction = """To find out more information about \
your pokemon: type the name or your favourite ID: \n\
For e.g.: key in pikachu or 25 to find out more about pikachu"""

while True:
    if first_load:
        print(instruction)
    first_load = False

    x = input()
    if x == "exit":
        exit()
    if x == "":
        print("Please key in something, trainer!")
    else:
        # TODO:
        try:
            result = search_db_or_api(x)
            print(result)
        except PokemonNotFoundError:
            print("Poke not found... Please try again, trainer!")

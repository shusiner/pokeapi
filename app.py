from interact_db import load_db, search_db
from interact_api import search_api

first_load = True

instruction = """To find out more information about \
your pokemon: type the name or your favourite ID: \n\
For e.g.: key in pikachu or 25 to find out more about pikachu"""
load_db()

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
        result = search_db(x)
        if result:
            pass
        else:
            search_api(x)
        # search for the input from db.txt
        if x == "25" or x == "pikachu":
            print("Pika!")
        else:
            print("Poke not found... Please try again, trainer!")

# This file is to interact with db and our db is in db.txt
import csv
import json
from os.path import exists


# this will return two object in a list
# 0: location areas
# 1: list of pokemon in cache
def load_db() -> list:
    with open('location_areas.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    # create the file if it does not exists
    with open('db.json', 'w+') as f:
        try:
            g = json.load(f)
        except:
            g = []
    return [[ i[0] for i in data], g]

# We can update db in two ways:
# 1. insert the record at the back
# 2. insert follow the string index
# 3. dump the whole list of json
# For now we will use method three as it is the easiest to implement
def update_db(pokemon_cached: list) -> None:
    with open('db.json', 'w') as f:
        json.dump(pokemon_cached,f)



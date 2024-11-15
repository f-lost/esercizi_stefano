import json, requests, random

def show_random_pokemon():
    id = random.randint(1,1025)

    url = f"https://pokeapi.co/api/v2/pokemon/{id}"

    response = requests.get(url)
    data = response.json()

    return (str(id), {"nome" : data["forms"][0],
            "abilità" : data["abilities"],
            "xp" : data["base_experience"],
            "altezza" : data["height"],
            "peso" : data["weight"]})


pokedex = {}
id, random_pokemon = show_random_pokemon()

if random_pokemon in pokedex:

    print("Pokemon già catturato.")

else:

    pokedex[id] = random_pokemon

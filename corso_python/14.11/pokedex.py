import json, requests, random
from pprint import pprint

pokedex_file = "pokedex.json"

def carica_pokedex():
    
    try:
        
        with open(pokedex_file,"r") as file:
            pokedex = json.load(file)
        
        return pokedex

    except:

        print("File pokedex non trovato.") 
        pokedex = {}
        print("File pokedex creato.")

        return pokedex
    


def salva_pokedex(pokedex):
    
    
    with open(pokedex_file, "w") as file:
        json.dump(pokedex, file)


def show_random_pokemon():
    id = random.randint(1,1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"

    response = requests.get(url)
    data = response.json()

    return (str(id), {"nome" : data["forms"][0]["name"],
            "abilità" : data["abilities"],
            "xp" : data["base_experience"],
            "altezza" : data["height"],
            "peso" : data["weight"]})

##########################


pokedex = carica_pokedex()

pprint(pokedex)

id, random_pokemon = show_random_pokemon()

print(f"{random_pokemon['nome']} è apparso!")
scelta = input("Vuoi catturarlo?: ").lower()

if scelta == "y":
    if id in pokedex:

        print("Pokemon già catturato.")

    else:
        
            pokedex[id] = random_pokemon

else:
     
     print(f"{random_pokemon["nome"]} va via.")


salva_pokedex(pokedex)

pprint(pokedex)

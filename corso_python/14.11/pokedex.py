import json, requests, random
from pprint import pprint

class Pokedex():



    def pokemon_iniziale(self):
        id = random.randint(1,1025)
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        if id not in pokedex:
                    
            pokedex[id] = random_pokemon

    def cattura_pokemon(self, pokemon):

        if scelta == "y":
            if id in pokedex:

                print("Pokemon già catturato.")

            else:
                
                    pokedex[id] = random_pokemon

        else:
            
            print(f"{random_pokemon['nome']} va via.")

    def carica_pokedex():
    
        try:
            pokedex_file = "pokedex.json"
            with open(pokedex_file,"r") as file:
                pokedex = json.load(file)
            
            return pokedex
        
        except:
            print("File pokedex non trovato.") 
            pokedex = {}
            print("File pokedex creato.")

            return pokedex

    def salva_pokedex(pokedex):

        pokedex_file = "pokedex.json"
        with open(pokedex_file, "w") as file:
            json.dump(pokedex, file)

    def stampa():
        
        pass

class Gioco():


    def show_random_pokemon():

        id = random.randint(1,1025)
        pokemon = Pokemon(id)
        print(f"{pokemon.nome} è apparso!")
        scelta = input("Vuoi catturarlo?: ").lower()

        

        return pokemon

        
    def inizia_battaglia(self, pokemon1, pokemon2):
        pass




class Pokemon():

    def __init__(self, id):

        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(url)
        data = response.json()
        self.nome = data["forms"][0]["name"]
        self.hp = data["stats"][0]["base_stats"]
        self.abilità = data["abilities"]
        self.xp = data["base_experience"]
        self.altezza = data["height"]
        self.peso = data["weight"]
        self.abilità_attiva = None
        self.attacco =  data["stats"][1]["base_stats"]
        self.difesa =  data["stats"][2]["base_stats"]
        #self.tipo = data["types"][0]["type"]["name"]

    def abilità_attive(self):

        for i in range(self.abilità):
            if self.abilità[i]["is_hidden"] == "true":
                self.abilità_attiva = self.abilità[i]["ability"]["name"]








    




##########################





# id, random_pokemon = show_random_pokemon()

# print(f"{random_pokemon['nome']} è apparso!")
# scelta = input("Vuoi catturarlo?: ").lower()

# if scelta == "y":
#     if id in pokedex:

#         print("Pokemon già catturato.")

#     else:
        
#             pokedex[id] = random_pokemon

# else:
     
#      print(f"{random_pokemon['nome']} va via.")


# salva_pokedex(pokedex)

# pprint(pokedex)


'''menù: 1- Cerca pokemon --> pokemon selvatico = show_random_pokemon() --> Lo vuoi catturare? Y->2, N->3
        2- avvia battaglia attacco -> scelta_pokemon_nel pokedex -->inizia_battaglia(self, nostro_pokemon, pokemon_selvatico) difesa-attacco -->
        3- scappa --> torna inizio menù

        '''



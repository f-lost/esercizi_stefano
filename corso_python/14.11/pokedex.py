import json, requests, random
from pprint import pprint

class Pokedex():

    def __init__(self,nome = "Pokedex"):

        self.nome = nome
        self.pokedex = self.carica_pokedex()

    def aggiungi_pokemon(self, pokemon_selvatico):
        
        for elemento in self.pokedex:

            if pokemon_selvatico.id not in elemento:
                        
                self.pokedex[pokemon_selvatico.id] = {"nome" : pokemon_selvatico.nome,
                                    "hp": pokemon_selvatico.hp,
                                    "abilità" : pokemon_selvatico.abilità,
                                    "xp" : pokemon_selvatico.xp,
                                    "altezza" : pokemon_selvatico.altezza,
                                    "peso" : pokemon_selvatico.peso,
                                    "abilità_attiva" : pokemon_selvatico.abilità_attiva,
                                    "attacco" : pokemon_selvatico.attacco,
                                    "difesa" : pokemon_selvatico.difesa}
                print(f"{pokemon_selvatico.nome} aggiunto al {self.nome}!")


    def pokemon_iniziale(self):


        if self.pokedex != {}:

            id = random.randint(1,1025)
            pokemon = Pokemon(id)

            if id not in self.pokedex:
                        
                self.pokedex[id] = {"nome" : pokemon.nome,
                                    "hp": pokemon.hp,
                                    "abilità" : pokemon.abilità,
                                    "xp" : pokemon.xp,
                                    "altezza" : pokemon.altezza,
                                    "peso" : pokemon.peso,
                                    "abilità_attiva" : pokemon.abilità_attiva,
                                    "attacco" : pokemon.attacco,
                                    "difesa" : pokemon.difesa}

    def cattura_pokemon(self, pokemon_selvatico, scelta):

        if scelta == "y":

            self.aggiungi_pokemon(self, pokemon_selvatico)

        else:
            
            print(f"{pokemon_selvatico.nome} va via.")

    def carica_pokedex():
    
        try:
            pokedex_file = "pokedex.json"
            with open(pokedex_file,"r") as file:
                pokedex = json.load(file)
            
            return pokedex
        
        except:
            print("File pokedex non trovato, creazione in corso.") 
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
        pokemon_selvatico = Pokemon(id)
        print(f"{pokemon_selvatico.nome} è apparso!")
        scelta = input("Vuoi provare a catturarlo?: ").lower()

        return scelta

        
    def inizia_battaglia(self, pokemon1, pokemon2):
        pass




class Pokemon():

    def __init__(self, id):

        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(url)
        data = response.json()
        self.nome = data["forms"][0]["name"]
        self.id = id
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



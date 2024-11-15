import json, requests, random
from pprint import pprint

class Pokedex():

    def __init__(self,nome = "Pokedex"):

        self.nome = nome
        self.pokedex = self.carica_pokedex()

    def aggiungi_pokemon(self, pokemon_selvatico):

        if pokemon_selvatico.id not in self.pokedex:
                    
            self.pokedex[pokemon_selvatico.id] = {"nome" : pokemon_selvatico.nome,
                                "hp": pokemon_selvatico.hp,
                                "xp" : pokemon_selvatico.xp,
                                "altezza" : pokemon_selvatico.altezza,
                                "peso" : pokemon_selvatico.peso,
                                "attacco" : pokemon_selvatico.attacco,
                                "difesa" : pokemon_selvatico.difesa}
            print(f"{pokemon_selvatico.nome} aggiunto al {self.nome}!")

    # def cattura_pokemon(self, pokemon_selvatico, scelta):

    #     if scelta == "y":

    #         self.aggiungi_pokemon(self, pokemon_selvatico)

    #     else:
            
    #         print(f"{pokemon_selvatico.nome} va via.")

    def pokemon_iniziale(self):

        if self.pokedex == {}:

            id = random.randint(500,1025)
            pokemon = Pokemon(id)

            if id not in self.pokedex:
                        
                self.pokedex[id] = {"nome" : pokemon.nome,
                                    "hp": pokemon.hp,
                                    "xp" : pokemon.xp,
                                    "altezza" : pokemon.altezza,
                                    "peso" : pokemon.peso,
                                    "attacco" : pokemon.attacco,
                                    "difesa" : pokemon.difesa}



    def carica_pokedex(self):
    
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

    def salva_pokedex(self):

        pokedex_file = "pokedex.json"
        with open(pokedex_file, "w") as file:
            json.dump(self.pokedex, file)

    def stampa(self):

        pprint(self.pokedex)


class Gioco():

    def show_random_pokemon(self):

        id = random.randint(1,1025)
        pokemon = Pokemon(id)
        print(f"{pokemon.nome} è apparso!")

        return pokemon


        
    def inizia_battaglia(self, nostro_pokemon, pokemon_selvatico, pokedex):
        
        if nostro_pokemon.attacco > pokemon_selvatico.difesa:
            print(f"{pokemon_selvatico.nome} selvatico è stato sconfitto! Catturiamolo!")
            pokedex.aggiungi_pokemon(pokemon_selvatico)
        else:
            print(f"Il nostro {nostro_pokemon.nome} è stato sconfitto! {pokemon_selvatico.nome} selvatico è scappato!")

    def gioca(self):

        pokedex = Pokedex()
        pokedex.pokemon_iniziale()
        
        while True:
            print("\n--- Benvenuto nel Gioco Pokémon ---")
            
            scelta = input("1. Cerca un nuovo Pokémon\n2. Mostra il Pokedex\n3. Esci\nScegli: ")

            if scelta == "1":
                selvatico = self.show_random_pokemon()
                catturato = input(f"Vuoi affrontare {selvatico.nome}? (y/n): ").lower()
                if catturato == "y":
                    # Usa un Pokémon del Pokedex per la lotta
                    if pokedex.pokedex:
                        tuo_pokemon_id = random.choice(list(pokedex.pokedex.keys()))
                        tuo_pokemon = Pokemon(tuo_pokemon_id)

                        self.inizia_battaglia(tuo_pokemon, selvatico, pokedex)
                    else:
                        print("Non hai Pokémon nella tua squadra!")

            elif scelta == "2":
                pokedex.stampa()

            elif scelta == "3":
                print("Grazie per aver giocato!")
                pokedex.salva_pokedex()
                break

            else:
                print("Scelta non valida. Riprova.")


class Pokemon():

    def __init__(self, id):

        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(url)
        data = response.json()
        self.nome = data["forms"][0]["name"]
        self.id = id
        self.hp = data["stats"][0]["base_stat"]
        #self.abilità = data["abilities"]
        self.xp = data["base_experience"]
        self.altezza = data["height"]
        self.peso = data["weight"]
        #self.abilità_attiva = None
        self.attacco =  data["stats"][1]["base_stat"]
        self.difesa =  data["stats"][2]["base_stat"]
        #self.tipo = data["types"][0]["type"]["name"]

    def abilità_attive(self):

        for i in range(self.abilità):
            if self.abilità[i]["is_hidden"] == "true":
                self.abilità_attiva = self.abilità[i]["ability"]["name"]



# --- Avvio del gioco ---
if __name__ == "__main__":
    gioco = Gioco()
    gioco.gioca()

    




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



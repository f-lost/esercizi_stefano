'''obbiettivo: gestionale ad oggetti ripetibile che fa:

1) registrazione/login/salvataggio_dei_dati/esci

2)funzionalità, a chi ha fatto login associa un punteggio

questo punteggio ci dice a quante funzionalità può accedere
0 punti -> 1 funzionalità, 1 punto -> 2 funzionalità (base/facile) ecc ecc

MASSIMO 10 funzionalità (livelli di difficoltà)

classifica salvata
'''

import pprint, random

#Classe Menù
class Menù:
    def init(self):
        self.registrato = False
        self.options = {
            "1 -": "Registrati come nuovo utente",
            "2 -": "Inizia il gioco",
            "3 -": "Visualizza classifica",
            "4 -": "Guida ai giochi",
            "5 -": "Impostazioni profilo",
            "6 -": "Seleziona difficoltà",
            "7 -": "Visualizza record personali",
            "8 -": "Esci"
            }


class Utente:

    def __init__(self, nome):

        self.__nome = nome
        self.__punteggio = 0

    def get_nome(self):

        return self.__nome
    
    def __get_punteggio(self):

        return self.__punteggio
    
    def stampa_punteggio(self):

        print(self.__get_punteggio())


class Classifica:


    def __init__(self):

        self.__classifica = {}

    def __get_classifica(self):

        return self.__classifica
    
    def __set_classifica(self, utente, valore):

        if utente in self.__classifica:

            self.__classifica[utente.get_nome()].append(valore)

        else:

            print("Ora sei in classifica!")
            self.__classifica[utente.get_nome()] = [valore]
        
    def aggiungi_a_classifica(self, utente, valore):

        self.__set_classifica(utente, valore)

    def stampa_classifica(self):

        pprint.pprint(self.__get_classifica())


class Gioco:
    def init(self, nome):
        self.nome = nome

 
class IndovinaIlNumero(Gioco):

    def init(self):
        super().init("Indovina il Numero")

    def start(self):
        numero_segreto = random.randint(1, 100)
        tentativi = 0
        print("Benvenuto a 'Indovina il Numero'!")
        while True:
            tentativo = int(input("Indovina il numero (1-100): "))
            tentativi += 1
            if tentativo < numero_segreto:
                print("Troppo basso!")
            elif tentativo > numero_segreto:
                print("Troppo alto!")
                print(numero_segreto)
            else:
                print(f"Complimenti! Hai indovinato il numero in {tentativi} tentativi.")
                break



#Esempio di utilizzo
gioco1 = IndovinaIlNumero()
gioco1.start()




        

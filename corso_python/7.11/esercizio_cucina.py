'''creare una classe base PersonaleCucina e diverse classi
derivate che rappresentano differenti ruoli all'interno 
della cucina di un ristorante.
L'obiettivo è di utilizzare l'ereditarietà per 
condividere alcune caratteristiche comuni mentre 
si distinguono le responsabilità e le azioni specifiche
di ogni ruolo.

Classe PersonaleCucina:
Attributi:
nome (stringa)
età (intero)
Metodi:
lavora() (metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto)

Classi Derivate:
Chef:
Attributi aggiuntivi come specialità
(tipo di cucina in cui è specializzato)
Metodi come prepara_menu()
che dettaglia come lo chef crea nuovi piatti e menu

SousChef:
Metodi come gestisci_inventario() per gestire
l'inventario della cucina e assistere lo chef

CuocoLinea:
Metodi come cucina_piatto(nome_piatto) 
che specifica la preparazione di un piatto specifico
nella linea di produzione'''

from abc import ABC, abstractmethod

class PersonaleCucina(ABC):

    def __init__(self, nome : str, età : int):
        
        self.__nome = nome
        self.__età = età
        self.lista = []

    def get_nome(self):
        return self.__nome
    
    def get_età(self):
        return self.__età
    
    @abstractmethod
    def lavora(self):
        pass


class Chef(PersonaleCucina):

    def __init__(self, nome : str, età : int, specialità = ""):

        super().__init__(nome, età)
        self.__specialità = specialità

    def prepara_menu():
        pass

    def lavora(self):
        pass


class SousChef(PersonaleCucina):

    def __init__(self, nome : str, età : int):

        super().__init__(nome, età)

    def prepara_menu(self):
        pass

    def lavora(self):
        pass


class SousChef(PersonaleCucina):

    def __init__(self, nome : str, età : int):

        super().__init__(nome, età)

    def gestisci_inventario(self):
        pass

    def lavora(self):
        pass


class CuocoLinea(PersonaleCucina):

    def __init__(self, nome : str, età : int):

        super().__init__(nome, età)

    def cucina_piatto(self, nome_piatto):
        print(f"{self.nome} sta cucinando {nome_piatto}.")

    def lavora(self):
        pass
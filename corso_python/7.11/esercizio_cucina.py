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

'''Crea una classe ristorante con una lista di liste 
chiamata menu e una lista chiamata ordinazione, 
Nel menu ci devono essere X piatti composti ogniuno 
da una lista propria di ingredienti, 
e la lista ordinazione invece e composta dalle singole 
ordinazioni del cleinte, 
Servirrà quindi una classe cliente e ogni membro 
della cucina potrà servire solo X piatti.

EXTRA: aggiungi personale, budget e costi,
Feedback piatti e chef'''




from abc import ABC, abstractmethod
import pprint
import time


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

    def get_nome(self):

        return super().get_nome()
    
    def prepara_menu(self):
        pass

    def lavora(self, piatto):
        
        print(f"Lo Chef {self.get_nome()} sta preparando {piatto}...")
        time.sleep(2)
        print(f"{piatto} è pronto!")


class SousChef(PersonaleCucina):

    def __init__(self, nome : str, età : int):

        super().__init__(nome, età)

    def gestisci_inventario(self):
        pass

    def lavora(self, piatto):

        print(f"Il Sous Chef {self.get_nome()} sta preparando {piatto}...")
        time.sleep(2)
        print(f"{piatto} è pronto!")


class CuocoLinea(PersonaleCucina):

    def __init__(self, nome : str, età : int):

        super().__init__(nome, età)

    def cucina_piatto(self, nome_piatto):
        print(f"{self.nome} sta cucinando {nome_piatto}.")

    def lavora(self, piatto):

        print(f"Il Cuoco di Linea {self.get_nome()} sta preparando {piatto}...")
        time.sleep(2)
        print(f"{piatto} è pronto!")


class Cliente():

    def __init__(self, nome : str):

        self.__nome = nome
        self.__ordinazioni = []

    def __get_nome(self):

        return self.__nome
    
    def __get_ordinazioni(self):

        return self.__ordinazioni
    
    def __set_ordinazioni(self, piatto):

        self.__ordinazioni.append(piatto)
    
    def chiedi_menù(self, ristorante):

        ristorante.stampa_menù()

    def ordina(self, ristorante, piatto):

        if piatto in ristorante.menù:

            self.__set_ordinazioni(piatto)

            ristorante.ricevi_ordinazioni(self.__get_ordinazioni()[-1])

    
class Ristorante():

    def __init__(self, nome : str, brigata):

        self.__nome = nome
        self.menù = {"pasta al sugo":["pasta", "pomodori", "cipolla", "basilico", "parmigiano"], "cotoletta": ["pangrattato", "uovo", "carne"], "minestrone": ["carote", "cipolle", "patate", "pomodori", "fagioli","broccoli"]}
        self.ordinazioni = []
        self.__brigata = brigata

    def __get_nome(self):

        return self.__nome
    
    def __get_brigata(self):

        return self.__brigata
    
    def aggiungi_piatto(self, piatto, ingredienti):

        self.menù[piatto] = ingredienti
        print(f"{piatto} aggiunto al menù.")

    def rimuovi_piatto(self, piatto):

        if piatto in self.menù:

            self.menù.remove(piatto)
            print(f"{piatto} rimosso dal menù.")

        else:
            print(f"{piatto} non presente nel menù.")

    def stampa_menù(self):

        pprint.pprint(self.menù)
    
    def ricevi_ordinazioni(self, ordinazioni):

        nuova_ordinazione = [ordinazioni, 0] #0 perchè il piatto non è stato preparato
        self.ordinazioni.append(nuova_ordinazione)

    def manda_in_preparazione(self):

        for i in self.ordinazioni:

            if i[1] == 0:

                if i[0] == "pasta al sugo":

                    elemento_brigata = next((elem for elem in self.__get_brigata() if elem.__class__.__name__ == "Chef"), "Non c'è uno chef che possa prepararti il piatto.")
                    elemento_brigata.lavora(i[0])
                    

                elif i[0] == "cotoletta":

                    elemento_brigata = next((elem for elem in self.__get_brigata() if elem.__class__.__name__ == "SousChef"), "Non c'è un SousChef che possa prepararti il piatto.")
                    elemento_brigata.lavora(i[0])

                elif i[0] == "cotoletta":

                    elemento_brigata = next((elem for elem in self.__get_brigata() if elem.__class__.__name__ == "CucocoLinea"), "Non c'è un Cuoco di linea che possa prepararti il piatto.")
                    elemento_brigata.lavora(i[0])
                
                else:

                    print("Non abbiamo un membro della brigata che sappia fare il piatto.")
                
                i[1] = 1

    def aggiungi_cuoco_brigata(self, cuoco):

        self.__brigata.append(cuoco)


#test


chef = Chef("Gigi", 30, "panini")
souschef = SousChef("Antonio", 25)
cuocolinea = CuocoLinea("Stefano", 20)

brigata = [chef, souschef, cuocolinea]

ristorante = Ristorante("Da Stefano", brigata)

cliente = Cliente("Bob")

cliente.chiedi_menù(ristorante)
cliente.ordina(ristorante, "pasta al sugo")

ristorante.manda_in_preparazione()


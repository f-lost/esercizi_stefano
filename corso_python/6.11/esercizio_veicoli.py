#Team 1 gruppo Cosimo - Lorenzo - Roberta - Stefano


'''creare una classe base Veicolo con attributi comuni a tutti i veicoli e metodi per operazioni comuni 
come l'accensione e lo spegnimento. Derivando questa classe, creeranno specifiche classi per
 Auto, Furgone e Motocicletta, aggiungendo caratteristiche uniche per ciascun tipo di veicolo.
Infine, dovranno implementare una classe GestoreParcoVeicoli per amministrare l'insieme dei veicoli.

#Lorenzo
Classe Veicolo:
Attributi privati:
___marca (stringa)
_modello (stringa)
_anno (intero)
_accensione (booleano)
Metodi:
accendi(): cambia lo stato di _accensione a vero.
spegni(): cambia lo stato di _accensione a falso.


Classi Derivate:

#Cosimo
Auto:
Attributi aggiuntivi come _numero_porte
Metodo specifico come suona_clacson()
metodo astratto specifico

#Cosimo
Furgone:
Attributi per _capacità_carico
Metodo per carica() e scarica()
metodo astratto specifico

#Roberta
Motocicletta:
Attributo per _tipo (e.g., sportiva, touring)
Metodo per esegui_wheelie() se il tipo è sportivo
metodo astratto specifico

#Roberta
Barca:
Attributo _tipo (motore/non motore)
Metodo _accendi_motore 
metodo astratto specifico

#Stefano
Classe GestoreParcoVeicoli:
Attributi:
_veicoli: lista di tutti i veicoli.
Metodi:
aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
rimuovi_veicolo(__marca, modello): rimuove un veicolo specifico dalla lista.
lista_veicoli(): stampa un elenco di tutti i veicoli nel parco.'''


from abc import ABC, abstractmethod

#Classe Astratta e Attributi Privati
class Veicolo(ABC):

    def __init__(self, marca, modello, anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False

    #Metodo per accendere il veicolo
    def accendi(self):
        if not self._accensione:
            self._accensione = True
            print(f"{self._marca} - {self._modello} acceso")
        else:
            print(f"{self._marca} - {self._modello} è già acceso")

    #Metodo per spegnere il veicolo
    def spegni(self):
        if self._accensione:
            self._accensione = False
            print(f"{self._marca} - {self._modello} spento")
        else:
            print(f"{self._marca} - {self._modello} è già spento")

    #Restituisce i dettagli del veicolo
    def get_dettagli(self):
        print(f"marca: {self._marca}, Modello: {self._modello}, Anno: {self._anno}")

    #Metodo astratto che deve essere implementato dalle sottoclassi
    @abstractmethod
    def metodo_specifico(self):
        pass


class Auto(Veicolo):

    #Metodo Costruttore
    def __init__(self,marca, modello, anno,colore,numero_porte):

        super().__init__(marca, modello, anno)
        self.colore = colore
        self.numero_porte = numero_porte

    #Metodo proprio della classe Auto
    def suona_clacson(self):
        print("Stai suonando il clacson")

    #Metodo astratto che eredita dalla classe Veicolo
    def metodo_specifico(self):
        print("L'auto fa qualcosa")

    #Metodo proprio della classe Auto
    def info_veicolo(self):
        print(f"L'auto che stai guidando è di colore {self.colore} ed ha {self.numero_porte} porte")


class Furgone(Veicolo):

    #Metodo Costruttore
    def __init__(self,marca, modello, anno,colore,capacita_carico):

        super().__init__(marca, modello, anno)
        self.colore = colore
        self.capacita_carico = capacita_carico

    #Metodo proprio della classe Furgone
    def carica(self,peso):
        if peso > self.capacita_carico:
            print("Il peso da lei selezionato è troppo grande")
        else:
            print(f"Caricati {peso}kg di merce")

    #Metodo proprio della classe Furgone
    def scarica(self):
        if self.capacita_carico > 0:
            print("Stai scaricando")
        else:
            print("Non hai nulla da scaricare")

    #Metodo astratto che eredita dalla classe Veicolo
    def metodo_specifico(self):
        print("Il furgone fa qualcosa")

    #Metodo proprio della classe Furgone
    def info_veicolo(self):
        print(f"Il furgone che stai guidando è di colore {self.colore} ed ha una capacità di carico di {self.capacita_carico}kg")


class Motocicletta(Veicolo):

    #Metodo Costruttore
    def __init__(self,marca, modello, anno, tipo):
        
        super().__init__(marca, modello, anno)        
        self._tipo = tipo

    #Metodo proprio della classe Motocicletta
    def esegui_wheelie(self):

        if self._tipo.lower() == "sportiva":
            print(f"{self._modello} sta eseguendo un wheelie!")
        else:
            print(f"{self._modello} non è adatta per un wheelie.")

    #Metodo astratto che eredita dalla classe Veicolo
    def metodo_specifico(self):

        print("La motocicletta fa qualcosa")


class Barca(Veicolo):

    #Metodo Costruttore
    def __init__(self,marca, modello, anno, tipo):
       
        super().__init__(marca, modello, anno)
        self._tipo = tipo

    #Metodo proprio della classe Barca
    def accendi_motore(self):

        if self._tipo.lower() == "motore":
            print("Il motore è acceso.")
        else:
            print("è una barca a vela e non ha un motore da accendere.")

    #Metodo astratto che eredita dalla classe Veicolo
    def metodo_specifico(self):

        print("La barca fa qualcosa")


class GestoreParcoVeicoli:

    #Metodo Costruttore
    def __init__(self, nome):

        self._veicoli = []
        self.nome = nome

    #Metodo aggiungi veicolo incapsulato
    def __aggiungi_veicolo(self, veicolo):
        
        self._veicoli.append(veicolo)
        tipo_veicolo = veicolo.__class__.__name__
        print(f"{tipo_veicolo} aggiunto al parco veicoli '{self.nome}'.")
    
    #Metodo da richiamare 
    def aggiungi_veicolo(self, veicolo):

        self.__aggiungi_veicolo(veicolo)

    #Metodo rimuovi veicolo incapsulato
    def __rimuovi_veicolo(self, veicolo):

        if veicolo in self._veicoli:

            self._veicoli.remove(veicolo)
            tipo_veicolo = veicolo.__class__.__name__
            print(f"{tipo_veicolo} rimosso dal parco veicoli '{self.nome}'.")

        else:
            print(f"{tipo_veicolo} non presente nel parco veicoli '{self.nome}' ")

    #Metodo da richiamare
    def rimuovi_veicolo(self, veicolo):

        self.__rimuovi_veicolo(veicolo)

    #Metodo per stampare tutti i veicoli
    def lista_veicoli(self):

        print(f"L'intero parco veicoli '{self.nome}' è composto da:")
        for veicolo in self._veicoli:
            print(veicolo.__class__.__name__)




#test
auto = Auto("Audi","A4", 2010, "rossa",4)
furgone = Furgone("Mercedes","Boh",2010,"bianco",10)
moto = Motocicletta("BMW", "Boh",2010,"sportiva")
barca = Barca("Boh","ancora boh",2010,"motore")


gestore = GestoreParcoVeicoli("Team 1")


gestore.aggiungi_veicolo(auto)
gestore.aggiungi_veicolo(furgone)
gestore.aggiungi_veicolo(moto)
gestore.aggiungi_veicolo(barca)

auto.accendi()
auto.spegni()
auto.get_dettagli()

auto.suona_clacson()
auto.info_veicolo()

furgone.carica(5)
furgone.scarica()
furgone.info_veicolo()

moto.esegui_wheelie()

barca.accendi_motore()


auto.metodo_specifico()
furgone.metodo_specifico()
moto.metodo_specifico()
barca.metodo_specifico()


gestore.rimuovi_veicolo(barca)

gestore.lista_veicoli()
    
        

from abc import ABC, abstractmethod
import pprint
import time


class PersonaleCucina(ABC):
    """
    Classe base per il personale di cucina. Contiene attributi comuni come nome ed età,
    e un metodo astratto 'lavora' che deve essere implementato dalle classi derivate.
    """

    def __init__(self, nome: str, età: int):
        self.__nome = nome
        self.__età = età
        self.lista = []

    def get_nome(self):
        """Restituisce il nome del membro del personale."""
        return self.__nome

    def get_età(self):
        """Restituisce l'età del membro del personale."""
        return self.__età

    @abstractmethod
    def lavora(self):
        """Metodo astratto che definisce il tipo di lavoro svolto."""
        pass


class Chef(PersonaleCucina):
    """
    Classe derivata per rappresentare uno Chef. Aggiunge l'attributo 'specialità' e il metodo
    'prepara_menu' per creare nuovi piatti.
    """

    def __init__(self, nome: str, età: int, specialità=""):
        super().__init__(nome, età)
        self.__specialità = specialità

    def get_nome(self):
        """Restituisce il nome dello Chef, sovrascrive il metodo della classe base."""
        return super().get_nome()

    def prepara_menu(self):
        """Metodo che permette allo chef di preparare un nuovo menu."""
        pass

    def lavora(self, piatto):
        """Lo chef prepara un piatto."""
        print(f"Lo Chef {self.get_nome()} sta preparando {piatto}...")
        time.sleep(2)
        print(f"{piatto} è pronto!")


class SousChef(PersonaleCucina):
    """
    Classe derivata per rappresentare un SousChef. Gestisce l'inventario e assiste lo Chef nella preparazione dei piatti.
    """

    def __init__(self, nome: str, età: int):
        super().__init__(nome, età)

    def gestisci_inventario(self, ristorante):
        """Gestisce l'inventario della cucina, implementato a livello di ristorante."""
        for i in ristorante.menù:
            pass  # Gestione inventario non implementata

    def lavora(self, piatto):
        """Il SousChef prepara un piatto."""
        print(f"Il Sous Chef {self.get_nome()} sta preparando {piatto}...")
        time.sleep(2)
        print(f"{piatto} è pronto!")


class CuocoLinea(PersonaleCucina):
    """
    Classe derivata per rappresentare un Cuoco di Linea. Prepara piatti specifici nella linea di produzione.
    """

    def __init__(self, nome: str, età: int):
        super().__init__(nome, età)

    def cucina_piatto(self, nome_piatto):
        """Il cuoco cucina un piatto specifico."""
        print(f"{self.get_nome()} sta cucinando {nome_piatto}.")

    def lavora(self, piatto):
        """Il Cuoco di Linea prepara un piatto."""
        print(f"Il Cuoco di Linea {self.get_nome()} sta preparando {piatto}...")
        time.sleep(2)
        print(f"{piatto} è pronto!")


class Cliente:
    """
    Classe per rappresentare un cliente che può ordinare piatti dal ristorante.
    """

    def __init__(self, nome: str):
        self.__nome = nome
        self.__ordinazioni = []

    def __get_nome(self):
        """Restituisce il nome del cliente."""
        return self.__nome

    def __get_ordinazioni(self):
        """Restituisce le ordinazioni del cliente."""
        return self.__ordinazioni

    def __set_ordinazioni(self, piatto):
        """Aggiunge un piatto all'ordinazione del cliente."""
        self.__ordinazioni.append(piatto)

    def chiedi_menù(self, ristorante):
        """Chiede al ristorante di stampare il menù."""
        ristorante.stampa_menù()

    def ordina(self, ristorante, piatto):
        """Il cliente ordina un piatto dal ristorante."""
        if piatto in ristorante.menù:
            self.__set_ordinazioni(piatto)
            ristorante.ricevi_ordinazione(self.__get_ordinazioni()[-1])


class Ristorante:
    """
    Classe per rappresentare un ristorante che ha un menù, una brigata di cucina e gestisce le ordinazioni.
    """

    def __init__(self, nome: str, brigata):
        self.__nome = nome
        # Menù predefinito
        self.menù = {
            "pasta al sugo": ["pasta", "pomodori", "cipolla", "basilico", "parmigiano"],
            "cotoletta": ["pangrattato", "uovo", "carne"],
            "minestrone": ["carote", "cipolle", "patate", "pomodori", "fagioli", "broccoli"]
        }
        self.__ordinazioni = []
        self.__brigata = brigata
        self.__inventario = []

    def __get_nome(self):
        """Restituisce il nome del ristorante."""
        return self.__nome

    def __get_brigata(self):
        """Restituisce la brigata di cucina."""
        return self.__brigata

    def _get_inventario(self):
        """Restituisce l'inventario del ristorante."""
        return self.__inventario

    def __get_ordinazioni(self):
        """Restituisce le ordinazioni ricevute."""
        return self.__ordinazioni

    def __set_ordinazione(self, nuova_ordinazione):
        """Aggiunge una nuova ordinazione alla lista delle ordinazioni."""
        self.__ordinazioni.append(nuova_ordinazione)

    def aggiungi_piatto(self, piatto, ingredienti):
        """Aggiunge un nuovo piatto al menù."""
        self.menù[piatto] = ingredienti
        print(f"{piatto} aggiunto al menù.")

    def rimuovi_piatto(self, piatto):
        """Rimuove un piatto dal menù."""
        if piatto in self.menù:
            self.menù.remove(piatto)
            print(f"{piatto} rimosso dal menù.")
        else:
            print(f"{piatto} non presente nel menù.")

    def stampa_menù(self):
        """Stampa il menù del ristorante."""
        pprint.pprint(self.menù)

    def ricevi_ordinazione(self, ordinazione):
        """Riceve una nuova ordinazione dal cliente."""
        nuova_ordinazione = [ordinazione, 0]  # 0 perché il piatto non è stato preparato
        self.__set_ordinazione(nuova_ordinazione)

    def manda_in_preparazione(self):
        """Invia le ordinazioni in preparazione, assegnando i piatti ai membri della brigata."""
        for i in self.__get_ordinazioni():
            if i[1] == 0:
                if i[0] == "pasta al sugo":
                    elemento_brigata = next((elem for elem in self.__get_brigata() if elem.__class__.__name__ == "Chef"), "Non c'è uno chef che possa prepararti il piatto.")
                    elemento_brigata.lavora(i[0])

                elif i[0] == "cotoletta":
                    elemento_brigata = next((elem for elem in self.__get_brigata() if elem.__class__.__name__ == "SousChef"), "Non c'è un SousChef che possa prepararti il piatto.")
                    elemento_brigata.lavora(i[0])

                elif i[0] == "minestrone":
                    elemento_brigata = next((elem for elem in self.__get_brigata() if elem.__class__.__name__ == "CuocoLinea"), "Non c'è un Cuoco di linea che possa prepararti il piatto.")
                    elemento_brigata.lavora(i[0])

                else:
                    print("Non abbiamo un membro della brigata che sappia fare il piatto.")
                i[1] = 1

    def aggiungi_cuoco_brigata(self, cuoco):
        """Aggiunge un membro alla brigata di cucina."""
        self.__brigata.append(cuoco)


# Test
chef = Chef("Gigi", 30, "panini")
souschef = SousChef("Antonio", 25)
cuocolinea = CuocoLinea("Stefano", 20)

brigata = [chef, souschef, cuocolinea]

ristorante = Ristorante("Da Stefano", brigata)

cliente = Cliente("Bob")

# Il cliente consulta il menù e ordina dei piatti
cliente.chiedi_menù(ristorante)
cliente.ordina(ristorante, "pasta al sugo")
cliente.ordina(ristorante, "cotoletta")
cliente.ordina(ristorante, "minestrone")

# Inizio della preparazione delle ordinazioni
ristorante.manda_in_preparazione

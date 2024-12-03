class Prodotto:
    """
    Classe che rappresenta un prodotto generico con informazioni di costo, prezzo e quantità.
    """

    def __init__(self, nome, costo_produzione, prezzo_vendita, quantità=1):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.quantità = quantità

    def calcola_profitto(self):
        """
        Calcola e stampa il profitto per singola unità venduta.
        """
        profitto = self.prezzo_vendita - self.costo_produzione
        print(f"Il profitto derivante dalla vendita di {self.nome} è di {profitto}€")

    def quanti(self):
        """
        Stampa la quantità disponibile del prodotto.
        """
        print(f"Ci sono {self.quantità} {self.nome}")


class Elettronica(Prodotto):
    """
    Sottoclasse per prodotti elettronici, include una garanzia.
    """

    def __init__(self, nome, costo_produzione, prezzo_vendita, quantità=1):
        super().__init__(nome, costo_produzione, prezzo_vendita, quantità)
        self.__garanzia = ""

    def set_garanzia(self, garanzia):
        """
        Imposta il valore della garanzia.
        """
        self.__garanzia = garanzia

    def get_garanzia(self):
        """
        Restituisce il valore della garanzia.
        """
        return self.__garanzia


class Abbigliamento(Prodotto):
    """
    Sottoclasse per prodotti di abbigliamento, include un materiale.
    """

    def __init__(self, nome, costo_produzione, prezzo_vendita, quantità=1):
        super().__init__(nome, costo_produzione, prezzo_vendita, quantità)
        self.__materiale = ""

    def set_materiale(self, materiale):
        """
        Imposta il materiale dell'abbigliamento.
        """
        self.__materiale = materiale

    def get_materiale(self):
        """
        Restituisce il materiale dell'abbigliamento.
        """
        return self.__materiale


class Accessoristica(Prodotto):
    """
    Sottoclasse per accessori, include un colore.
    """

    def __init__(self, nome, costo_produzione, prezzo_vendita, quantità=1):
        super().__init__(nome, costo_produzione, prezzo_vendita, quantità)
        self.__colore = ""

    def set_colore(self, colore):
        """
        Imposta il colore dell'accessorio.
        """
        self.__colore = colore

    def get_colore(self):
        """
        Restituisce il colore dell'accessorio.
        """
        return self.__colore


class Fabbrica:
    """
    Classe che rappresenta una fabbrica con un inventario di prodotti.
    """

    def __init__(self, nome):
        self.inventario = {}
        self.nome = nome

    def aggiungi_prodotto(self, prodotto):
        """
        Aggiunge un prodotto all'inventario o incrementa la sua quantità.
        """
        if prodotto.nome in self.inventario.keys():
            self.inventario[prodotto.nome] += 1
        else:
            self.inventario[prodotto.nome] = 1
        print(f"Prodotto aggiunto con successo: {self.inventario[prodotto.nome]} {prodotto.nome} presenti in inventario.")

    def vendi_prodotto(self, prodotto):
        """
        Rimuove una unità di un prodotto dall'inventario, se disponibile, e calcola il profitto.
        """
        if prodotto.nome in self.inventario.keys() and self.inventario[prodotto.nome] > 0:
            self.inventario[prodotto.nome] -= 1
            prodotto.calcola_profitto()
            print(f"Vendita effettuata: {self.inventario[prodotto.nome]} {prodotto.nome} presenti in inventario.")
        else:
            print("Prodotto non presente o esaurito.")

    def resi_prodotto(self, prodotto):
        """
        Aggiunge una unità di un prodotto all'inventario come reso.
        """
        if prodotto.nome in self.inventario.keys():
            self.inventario[prodotto.nome] += 1
            print(f"Reso effettuato: {self.inventario[prodotto.nome]} {prodotto.nome} presenti in inventario.")
        else:
            print("Prodotto non presente in inventario.")

    def stampa_inventario(self):
        """
        Stampa l'inventario completo della fabbrica.
        """
        print(f"L'inventario di '{self.nome}' è il seguente:\n")
        for prodotto, quantità in self.inventario.items():
            print(f"{prodotto}: {quantità}")


def calcola_profitto(prodotto):
    """
    Funzione per calcolare il profitto, se l'oggetto è di tipo Prodotto.
    """
    if isinstance(prodotto, Prodotto):
        prodotto.calcola_profitto()
    else:
        print("Tipo non supportato")


def quantità(prodotto):
    """
    Funzione per stampare la quantità di un prodotto, se valido.
    """
    if isinstance(prodotto, Prodotto):
        prodotto.quanti()
    else:
        print("Tipo non supportato")


def stampa_caratteristica(prodotto):
    """
    Stampa una caratteristica speciale del prodotto (garanzia, materiale o colore).
    """
    caratteristiche = {"garanzia", "materiale", "colore"}
    for caratteristica in caratteristiche:
        metodo = f"get_{caratteristica}"
        if hasattr(prodotto, metodo):
            valore = getattr(prodotto, metodo)()
            print(f"{prodotto.nome} ha {caratteristica}: {valore}")
            break


# Test della classe e delle funzioni
fab1 = Fabbrica("Fabbrica di Prova")

prodotto1 = Prodotto("Prodotto1", 10, 100, 5)
prodotto2 = Prodotto("Prodotto2", 2, 10, 10)

pc = Elettronica("Lenovo", 100, 200)
pc.set_garanzia(4)

maglietta = Abbigliamento("Adidas", 5, 20)
maglietta.set_materiale("cotone")

occhiali = Accessoristica("Polaroid", 8, 20)
occhiali.set_colore("rossi")

# Calcolo del profitto
prodotto1.calcola_profitto()
pc.calcola_profitto()
maglietta.calcola_profitto()
occhiali.calcola_profitto()

# Operazioni sull'inventario
fab1.aggiungi_prodotto(prodotto1)
fab1.aggiungi_prodotto(prodotto2)
fab1.aggiungi_prodotto(maglietta)
fab1.aggiungi_prodotto(pc)
fab1.aggiungi_prodotto(occhiali)

fab1.vendi_prodotto(prodotto1)
fab1.vendi_prodotto(occhiali)

fab1.resi_prodotto(prodotto1)

fab1.stampa_inventario()

# Test funzioni generiche
calcola_profitto(prodotto1)
calcola_profitto(occhiali)
quantità(occhiali)
quantità(prodotto1)

stampa_caratteristica(occhiali)
stampa_caratteristica(maglietta)

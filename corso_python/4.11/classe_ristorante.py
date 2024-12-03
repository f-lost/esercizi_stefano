class Ristorante:
    """
    Classe che rappresenta un ristorante con nome, tipo di cucina, stato (aperto/chiuso) e menu.
    """

    def __init__(self, nome, tipo_cucina):
        """
        Inizializza il ristorante con nome, tipo di cucina, stato chiuso e menu vuoto.
        """
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}  # Dizionario per piatti e prezzi

    def descrivi_ristorante(self):
        """Descrive il ristorante con il nome e il tipo di cucina."""
        print(f"'{self.nome}' è un ristorante {self.tipo_cucina}")

    def stato_apertura(self):
        """Mostra lo stato attuale del ristorante (aperto o chiuso)."""
        if self.aperto:
            print(f"Il ristorante '{self.nome}' è aperto")
        else:
            print(f"Il ristorante '{self.nome}' è chiuso")

    def apri_ristorante(self):
        """Apre il ristorante e aggiorna lo stato."""
        self.aperto = True
        print(f"Il ristorante '{self.nome}' è ora aperto")

    def chiudi_ristorante(self):
        """Chiude il ristorante e aggiorna lo stato."""
        self.aperto = False
        print(f"Il ristorante '{self.nome}' è ora chiuso")

    def aggiungi_al_menu(self, piatto, prezzo):
        """
        Aggiunge un piatto al menu con il relativo prezzo.
        Se il piatto esiste già, notifica l'utente.
        """
        if piatto in self.menu:
            print("Piatto già presente nel menù di", self.nome)
        else:
            self.menu[piatto] = prezzo
            print(f"{piatto} aggiunto al menù di '{self.nome}'")

    def togli_dal_menu(self, piatto):
        """
        Rimuove un piatto dal menu.
        Se il piatto non esiste, notifica l'utente.
        """
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"{piatto} rimosso dal menù di '{self.nome}'")
        else:
            print("Piatto non presente nel menù di", self.nome)

    def stampa_menu(self):
        """Stampa il menu completo del ristorante."""
        print(f"Il menù di '{self.nome}' è il seguente:\n")
        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: {prezzo}€")


# Test della classe Ristorante
ristorante1 = Ristorante("Ciao Pizza", "Pizzeria")

ristorante1.descrivi_ristorante()
ristorante1.stato_apertura()

ristorante1.apri_ristorante()
ristorante1.stato_apertura()

ristorante1.chiudi_ristorante()
ristorante1.stato_apertura()

ristorante1.aggiungi_al_menu("pizza", "5")
ristorante1.stampa_menu()

ristorante1.togli_dal_menu("pizza")
ristorante1.stampa_menu()

class Ristorante:


    def __init__(self,nome,tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {} #piatti e prezzi

    def descrivi_ristorante(self):
        print(f"'{self.nome}' è un ristorante {self.tipo_cucina}")

    def stato_apertura(self):
        if self.aperto is True:
            print(f"Il ristorante '{self.nome}' è aperto")
        else:
            print(f"Il ristorante '{self.nome}' è chiuso")

    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante '{self.nome}' è ora aperto")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante '{self.nome}' è ora chiuso")

    def aggiungi_al_menu(self, piatto, prezzo):
        if piatto in self.menu:
            print("Piatto già presente nel menù di ", self.nome)
        else:
            self.menu[piatto] = prezzo
            print(f"{piatto} aggiunto al menù di '{self.nome}'")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"{piatto} rimosso dal menù di '{self.nome}'")
        else:
            print("Piatto non presente nel menù di", self.nome)

    def stampa_menu(self):
        print(f"Il menù di '{self.nome}' è il seguente:\n")
        print(self.menu)




#test


ristorante1 = Ristorante("Ciao Pizza","Pizzeria")

ristorante1.descrivi_ristorante()

ristorante1.stato_apertura()

ristorante1.apri_ristorante()

ristorante1.stato_apertura()

ristorante1.chiudi_ristorante()

ristorante1.stato_apertura()

ristorante1.aggiungi_al_menu("pizza","5")

ristorante1.stampa_menu()

ristorante1.togli_dal_menu("pizza")

ristorante1.stampa_menu()

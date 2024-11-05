class Prodotto:

    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        print(f"Il profitto derivante dalla vendita di {self.nome} è di {profitto}€")
    

class Fabbrica:
    
    def __init__(self, nome):
        self.inventario = {}
        self.nome = nome
    
    def aggiungi_prodotto(self,prodotto):
        if prodotto.nome in self.inventario.keys():
            self.inventario[prodotto.nome] += 1
            print(f"Prodotto aggiunto con successo: {prodotto.nome} è ora presente in inventario.")
            
        else:
            self.inventario[prodotto.nome] = 1
            print(f"Prodotto aggiunto con successo: {self.inventario[prodotto.nome]} {prodotto.nome} presenti in inventario.")

    def vendi_prodotto(self, prodotto):
        if prodotto.nome in self.inventario.keys() and self.inventario[prodotto.nome] != 0:
            self.inventario[prodotto.nome] -= 1
            prodotto.calcola_profitto()
            print(f"Vendita effettuata: {self.inventario[prodotto.nome]} {prodotto.nome} presenti in inventario.")
        else:
            print("Prodotto non presente")

    def resi_prodotto(self, prodotto):
        if prodotto.nome in self.inventario.keys():
            self.inventario[prodotto.nome] += 1
            print(f"Reso effettuato: {self.inventario[prodotto.nome]} {prodotto.nome} presenti in inventario.")
        else:
            print("Prodotto non presente")

    def stampa_inventario(self):
        print(f"L'inventario di '{self.nome}' è il seguente:\n")
        for prodotto, quantità in self.inventario.items():
            print(f"{prodotto}: {quantità}")


class Elettronica(Prodotto):
    
    def __init__(self,nome,costo_produzione,prezzo_vendita, garanzia):

        Prodotto.__init__(self,nome,costo_produzione,prezzo_vendita)
        self.garanzia = garanzia


class Abbigliamento(Prodotto):

    def __init__(self,nome,costo_produzione,prezzo_vendita, materiale):

        Prodotto.__init__(self,nome,costo_produzione,prezzo_vendita)
        self.materiale = materiale



#test

fab1 = Fabbrica("Fabbrica di Prova")

prodotto1 = Prodotto("Prodotto", 10, 100)
prodotto2 = Prodotto("Prodotto2", 2, 10)

prodotto1.calcola_profitto()

fab1.aggiungi_prodotto(prodotto1)
fab1.aggiungi_prodotto(prodotto2)

fab1.vendi_prodotto(prodotto1)

fab1.resi_prodotto(prodotto1)

fab1.stampa_inventario()


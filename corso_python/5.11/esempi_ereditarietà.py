class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

#Ereditarietà Singola
class Quad(Veicolo):

    pass

#Ereditarietà Multipla
class AutomobileSportiva(Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello) #con super() chiamo il primo padre, potevo fare super.__init__

        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self): 
        
        super().mostra_informazioni()
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()


auto_sportiva = AutomobileSportiva("Ferrari","F8",["ABS","Controllo Trazione", "Airbag Laterali"],720)
auto_sportiva.mostra_informazioni()
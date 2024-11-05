import math

class Punto:

    def __init__(self, x, y): #init è il metodo costuttore, è necessario e ha bisogno di self come placeholder
        self.x = x
        self.y = y

    def muovi(self,dx,dy):
        x += dx
        y += dy
    def distanza_da_origine(self):
        d = math.sqrt(self.x**2 + self.y**2)
        return d
    
class Libro:

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        print("Il libro ", self.titolo," è stato scritto da ", self.autore, " e ha ", self.pagine, " pagine.")
       

    
class Biblioteca:
    libri = []

    def __init__(self):
        libri = []

    def creazione(self):
        titolo= input(f"Come si chiama il libro?: ")
        autore = input(f"Chi ha scritto il libro?: ")
        pagine = input(f"Quante pagine ha il libro?: ")
        libri.append(Libro(titolo, autore, pagine))

    def stampa(self):
        pass
        

libro1 = Biblioteca.creazione(self)
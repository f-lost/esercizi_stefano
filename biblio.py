    
class Libro:

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        print("Il libro ", self.titolo," è stato scritto da ", self.autore, " e ha ", self.pagine, " pagine.")
       

    
class Biblioteca:
    

    def __init__(self):
        self.libri = []

    def creazione(self):
        titolo= input(f"Come si chiama il libro?: ")
        autore = input(f"Chi ha scritto il libro?: ")
        pagine = input(f"Quante pagine ha il libro?: ")
        
        nuovo_libro = Libro(titolo, autore, pagine)
        self.libri.append(nuovo_libro)

    def stampa(self):
        print(f"Nella biblioteca ci sono {len(self.libri)} libri")
        print("Lista dei libri in biblioteca:\n")
        for libro in self.libri:
            libro.descrizione() 


biblioteca = Biblioteca()

n = int(input("Quanti libri vuoi aggiungere?: "))

for i in range(n):
    biblioteca.creazione()


biblioteca.stampa()

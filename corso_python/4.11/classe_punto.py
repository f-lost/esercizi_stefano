import math


class Punto:
    """
    Classe che rappresenta un punto in uno spazio bidimensionale.
    """

    def __init__(self, x, y):
        """
        Inizializza un punto con coordinate x e y.
        """
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        """
        Muove il punto di un certo delta (dx, dy) rispetto alla posizione attuale.
        """
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        """
        Calcola e restituisce la distanza del punto dall'origine (0, 0).
        """
        return math.sqrt(self.x**2 + self.y**2)


class Libro:
    """
    Classe che rappresenta un libro con titolo, autore e numero di pagine.
    """

    def __init__(self, titolo, autore, pagine):
        """
        Inizializza un libro con titolo, autore e numero di pagine.
        """
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        """
        Stampa una descrizione del libro con titolo, autore e numero di pagine.
        """
        print(f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine.")

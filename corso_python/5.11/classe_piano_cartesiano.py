import math
import random

class PianoCartesiano:
    """
    Rappresenta un piano cartesiano con la possibilità di definire punti
    e calcolare rette tra di essi.
    """

    piano = []  # Lista dei punti sul piano

    def __init__(self):
        """
        Costruttore: chiede i primi 3 punti necessari per definire un piano.
        Il terzo punto deve essere indipendente dagli altri due.
        """
        print("Dammi le componenti dei primi 3 punti necessari a creare il piano\n")
        for i in range(2):
            p_x = float(input(f"P{i}_x: "))
            p_y = float(input(f"P{i}_y: "))
            self.piano.append(Punto(p_x, p_y))

        p_x = float(input(f"P3_x: "))
        p_y = float(input(f"P3_y: "))

        # Controllo di indipendenza del terzo punto
        while True:
            if (p_x - self.piano[0].x) * (self.piano[1].y - self.piano[0].y) != \
                    (self.piano[1].x - self.piano[0].x) * (p_y - self.piano[0].y):
                self.piano.append(Punto(p_x, p_y))
                break
            else:
                print("Punto dipendente dagli altri due, dammene uno indipendente per creare un piano.")
                p_x = float(input(f"P3_x: "))
                p_y = float(input(f"P3_y: "))

    def aggiungi_punto(self):
        """
        Permette di aggiungere uno o più punti al piano.
        """
        n = int(input("Quanti punti vuoi aggiungere?: "))
        print("Dammi le componenti\n")
        for i in range(n):
            p_x = float(input(f"P{i}_x: "))
            p_y = float(input(f"P{i}_y: "))
            self.piano.append(Punto(p_x, p_y))

    def stampa(self):
        """
        Stampa le coordinate di tutti i punti sul piano.
        """
        for i in range(len(self.piano)):
            print(f"({self.piano[i].x}, {self.piano[i].y})")

    def retta(self, a, b):
        """
        Calcola l'equazione della retta passante per due punti distinti.
        """
        if a.x != b.x and a.y != b.y:
            m = (b.y - a.y) / (b.x - a.x)  # Coefficiente angolare
            q = a.y - m * a.x  # Intercetta
            if q > 0:
                print(f"La retta passante per ({a.x}, {a.y}) e ({b.x}, {b.y}) è : y = {m}x + {q}")
            else:
                q = -q
                print(f"La retta passante per ({a.x}, {a.y}) e ({b.x}, {b.y}) è : y = {m}x - {q}")
        elif a.x == b.x and a.y != b.y:
            print(f"La retta passante per ({a.x}, {a.y}) e ({b.x}, {b.y}) è : x = {a.x}")
        elif a.y == b.y and a.x != b.x:
            print(f"La retta passante per ({a.x}, {a.y}) e ({b.x}, {b.y}) è : y = {a.y}")
        else:
            print("Dammi due punti distinti.")


class Punto:
    """
    Classe per rappresentare un punto sul piano cartesiano.
    """

    def __init__(self, x, y):
        """
        Costruttore: inizializza le coordinate del punto.
        """
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        """
        Sposta il punto di una quantità specifica lungo x e y.
        """
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        """
        Calcola la distanza del punto dall'origine (0, 0).
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

class Polinomio:
    """
    Classe per rappresentare un polinomio sul piano cartesiano.
    """

    def __init__(self, grado, coefficienti_interi=True):
        """
        Coefficienti_interi=True usa random.randint, settato a False usa random.uniform tra -50 e 50.
        """
            
        
        self.coefficienti = []
    
        if coefficienti_interi:

            for i in range(grado):
                coefficiente_i = random.randint(-50, 50)
                self.coefficienti.append(coefficiente_i)
        else:

            for i in range(grado):
                coefficiente_i = random.uniform(-50, 50)
                self.coefficienti.append(coefficiente_i)
            





# Test
xyz = PianoCartesiano()
xyz.stampa()

a = Punto(2, 3)
b = Punto(1, 2)

xyz.retta(a, b)

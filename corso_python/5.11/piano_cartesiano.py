import math


class PianoCartesiano:
    
    piano = []

    def __init__(self):

        print("Dammi le componenti dei primi 3 punti necessari a creare il piano\n")
        for i in range(2):
            p_x = float(input(f"P{i}_x: "))
            p_y = float(input(f"P{i}_y: "))
            self.piano.append(Punto(p_x,p_y))
        
        p_x = float(input(f"P{3}_x: "))
        p_y = float(input(f"P{3}_y: "))

        while True:
            if (p_x - self.piano[0].x)*(self.piano[1].y - self.piano[0].y) != (self.piano[1].x - self.piano[0].x)*(p_y - self.piano[0].y):
                self.piano.append(Punto(p_x,p_y))
                break
            else:
                print("Punto dipendente dagli altri due, dammene uno indipendente per creare un piano.")
                p_x = float(input(f"P{3}_x: "))
                p_y = float(input(f"P{3}_y: "))


    def aggiungi_punto(self):
        n = int(input("Quanti punti vuoi aggiungere?: "))
        print("Dammi le componenti\n")
        for i in range(n):
            p_x = float(input(f"P{i}_x: "))
            p_y = float(input(f"P{i}_y: "))
            self.piano.append(Punto(p_x,p_y))

    def stampa(self):
        for i in range(len(self.piano)):
            print(f"({self.piano[i].x},{self.piano[i].y})")

        


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
    

xyz = PianoCartesiano()
xyz.stampa()



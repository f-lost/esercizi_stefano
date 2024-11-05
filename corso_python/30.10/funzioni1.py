# def saluta(nome):
#     print("Ciao ", nome)

# def somma(a, b):
#     risultato = a + b
#     print("Il risultato è: ", risultato)


import random

def genera_random():
    r = random.randint(1, 100)
    choice = True
    n = int(input("Che numero casuale ho generato ( tra 1 e 100)?: "))

    while n != r and choice:
        if n > r:
            print("Il numero da indovinare è più piccolo.")
        else:
            print("Il numero da indovinare è più grande.")
        
        scelta = input("Vuoi continuare a provare? (y/n) ").lower()
        if scelta == "n" or scelta == "no":
            choice = False
        else:
            n = int(input("Che numero casuale ho generato?: "))

    if n == r:
        print("Complimenti! Hai indovinato il numero.")
    else:
        print("Peccato, il numero era ",r)



genera_random()


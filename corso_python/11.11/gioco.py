'''Part 1 Scrivete un programma che genera 5 numeri
casuali e li salva su un file,
part 2 il programma legge il file e l’utente
 dovrà cercare di indovinarne almeno 2 numero oppure
   avrà perso.'''


import random

def genera_e_salva():

    numeri_casuali = []

    for i in range(5):
        numero = random.randint(0,10)
        numeri_casuali.append(numero)
        

        with open("numeri_casuali.txt", "a") as file:
            file.write(str(numero) + ",")

    return numeri_casuali

def apri_e_indovina():

    contatore = 0
    with open("numeri_casuali.txt", "r") as file:
        contenuto = file.read().split(",")
        numeri_salvati = [int(num) for num in contenuto if num.isdigit()]

    for i in range(5):

        domanda = int(input(f"Indovina un numero, tentativo numero {i+1}: "))

        if domanda in numeri_salvati:
            contatore +=1
            print("Indovinato!")
            numeri_salvati.remove(domanda)
    
    if contatore >= 2:

        print(f"Hai vinto indovinando {contatore} numeri!")
    
    else:

        print(f"Hai perso indovinando {contatore} numeri!")
        
    with open("numeri_casuali.txt", "w") as file:
        pass

#test

numeri_casuali = genera_e_salva()

apri_e_indovina()

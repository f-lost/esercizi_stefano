'''Andare a svolger e in gruppo minimo 3:
Andiamo a creare un sistema a X fasi dove x è il numero dei partecipanti
il cui scopo e: loggare, controllare i dati,
far eseguire un "Gioco matematico a punteggio(numerico consiglio)"
da cui creare un classifica e un logout con possibilità 
di ripetizione

'''

import random
import time
users = {}

#gioco a tempo, meno ci metti più punti fai?
def gioco_equazioni(nome_utente):
    print(f"Ciao {nome_utente}! In questo gioco dovrai risolvere un'equazione di primo grado. Se il risultato è con la virgola approssima alle prime due cifre significative! FAI VELOCE!")

    a = 0
    while a == 0:
        a = random.randint(-10,10)

    b = random.randint(-100, 100)

    print(f"Risolvi l'equazione {a}x + {b} = 0 \n")

    sol = round(-b/a, 2)
    
    while True:
        t1 = time.time()
        #print(sol)
        x = float(input("Qual è la tua soluzione? "))
        x=round(x, 2)
        
        punteggio = time.time() - t1
        punteggio = round(punteggio, 3)
        if x  == sol:
            print(nome_utente, "ci hai messo ", punteggio, " secondi per completarlo!")
            break
        else:
            print("Ritenta!")

    return punteggio


#il gioco crea un numero da 1 a 100 e bisogna indovinarlo, il gioco
# ti dice se il numero immesso è più grande o più piccolo della soluzione

def gioco_random(nome_utente):
    print(f"Ciao {nome_utente}! In questo gioco dovrai indovinare un numero, inizia a dirne uno e io ti dirò se il numero da indovinare è più grande o più piccolo! FAI VELOCE!")
    r = random.randint(1, 100)
    
    while True:
        t1 = time.time()
        n = int(input("Che numero casuale ho generato ( tra 1 e 100)?: "))
        if n > r:
            print("Il numero da indovinare è più piccolo.")
        elif n < r:
            print("Il numero da indovinare è più grande.")
        else:
            punteggio = time.time() - t1
            punteggio = round(punteggio, 3)
            print("Complimenti " ,nome_utente, "! Ci hai messo ", punteggio, " secondi per completare il gioco!")
            return punteggio
    

#menù da chiamare che chiama a sua volta i due giochi di sopra
def menu_giochi(nome_utente):
    choice = int(input(f"Ciao {nome_utente}! A che gioco vuoi giocare?\n1)Indovina il numero\n2)Risolvi l'equazione\n:  " ))
    if choice == 1:
        punteggio = gioco_random(nome_utente)
    elif choice == 2:
        punteggio = gioco_equazioni(nome_utente)
    else:
        print("scelta non valida. Riprova.")

    return punteggio

#cosimo
def login(users):
    #print(users)
    nome_utente = input("Inserisci nome utente: ")
    pwd = input("Inserisci password: ")
    for id_utente, user in users.items():
        print(id_utente)
        print(user)
        if user["nome"] == nome_utente and user["password"] == pwd:
            print(f"Login effettuato per l'utente {nome_utente}")

            return True, nome_utente
        

    print(f"Nome utente o password sbagliata")
    return False, " "

#daniele
def classifica(users):
    classifica_users = users.copy()
    classifica_users = sorted(classifica_users.items(), key=lambda item: list(item[1].values())[1], reverse=True)
    index = 1
    for user in classifica_users:
        print(f"{index}° posto: {user[1]["nome"]} -> {user[1]["punteggio"]}")
        index += 1

#roberta
#registrazione
def registra_user(users):
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")

# Controlla se l'user è già registrato
# users.items() restituisce tutte le coppie (chiave, valore) del dizionario users.
# Il ciclo for itera su ciascuna coppia, assegnando la chiave a id_utente e il valore a dati.
# Può accedere agli ID user e ai dati associati (nome e password) all'interno del ciclo.
    for id_user, dati in users.items():
        if dati['nome'] == nome:
            print("user già registrato.")
            return

    # Genera un nuovo ID user
    id_user = len(users) + 1
    punteggio = 0
    users[id_user] = {'nome': nome, 'password': password , "punteggio": punteggio}
    print(f"Registrazione completata per {nome} con ID user {id_user}")

def main(users):
    

    while True:
        scegli = input("Inserisci 'registra' per registrarti, 'login' per loggarti o 'esci' per terminare: ").lower()
        if scegli == 'registra':
            registra_user(users)
        elif scegli == 'esci':
            break
        elif scegli == "login":
            result, nome = login(users)
            if result:
                punteggio = menu_giochi(nome)
                
                choice = input("Vuoi stampare la classifica? ( Y\\N): ").lower()
                if choice == "y" or choice == "yes":
                    classifica(users)
                    
        else:
            print("scelta non valido. Riprova.")


users = {}
main(users)


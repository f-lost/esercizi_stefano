'''Andare a svolger e in gruppo minimo 3:
Andiamo a creare un sistema a X fasi dove x è il numero dei partecipanti
il cui scopo e: loggare, controllare i dati,
far eseguire un "Gioco matematico a punteggio(numerico consiglio)"
da cui creare un classifica e un logout con possibilità 
di ripetizione

'''
import random
import time

# Dizionario per memorizzare gli utenti
users = {}


def gioco_equazioni(nome_utente):
    """
    Gioco per risolvere un'equazione di primo grado.
    Il punteggio dipende dalla velocità di risoluzione.
    """
    print(
        f"Ciao {nome_utente}! In questo gioco dovrai risolvere un'equazione di primo grado. "
        f"Se il risultato è con la virgola, approssima alle prime due cifre significative! FAI VELOCE!"
    )

    # Genera l'equazione casuale (a ≠ 0)
    a = 0
    while a == 0:
        a = random.randint(-10, 10)
    b = random.randint(-100, 100)

    print(f"Risolvi l'equazione {a}x + {b} = 0 \n")
    sol = round(-b / a, 2)

    while True:
        tempo_zero = time.time()  # Tempo iniziale
        x = float(input("Qual è la tua soluzione? "))
        x = round(x, 2)
        punteggio = round(time.time() - tempo_zero, 3)  # Tempo di risposta

        if x == sol:
            print(nome_utente, "ci hai messo", punteggio, "secondi per completarlo!")
            break
        else:
            print("Ritenta!")

    return punteggio


def gioco_random(nome_utente):
    """
    Gioco per indovinare un numero casuale.
    Il punteggio dipende dalla velocità di indovinare.
    """
    print(
        f"Ciao {nome_utente}! In questo gioco dovrai indovinare un numero. "
        f"Inizia a dirne uno e io ti dirò se il numero da indovinare è più grande o più piccolo! FAI VELOCE!"
    )

    r = random.randint(1, 100)  # Numero da indovinare

    while True:
        tempo_zero = time.time()  # Tempo iniziale
        n = int(input("Che numero casuale ho generato (tra 1 e 100)?: "))
        if n > r:
            print("Il numero da indovinare è più piccolo.")
        elif n < r:
            print("Il numero da indovinare è più grande.")
        else:
            punteggio = round(time.time() - tempo_zero, 3)  # Tempo di risposta
            print(
                "Complimenti", nome_utente, "! Ci hai messo", punteggio, "secondi per completare il gioco!"
            )
            return punteggio


def menu_giochi(nome_utente):
    """
    Mostra il menu dei giochi e gestisce la scelta dell'utente.
    """
    choice = int(
        input(
            f"Ciao {nome_utente}! A che gioco vuoi giocare?\n"
            f"1) Indovina il numero\n"
            f"2) Risolvi l'equazione\n:  "
        )
    )

    if choice == 1:
        return gioco_random(nome_utente)
    elif choice == 2:
        return gioco_equazioni(nome_utente)
    else:
        print("Scelta non valida. Riprova.")
        return None


def login(users):
    """
    Funzione di login: verifica le credenziali e autentica l'utente.
    """
    nome_utente = input("Inserisci nome utente: ")
    pwd = input("Inserisci password: ")

    for id_utente, user in users.items():
        if user["nome"] == nome_utente and user["password"] == pwd:
            print(f"Login effettuato per l'utente {nome_utente}")
            return True, nome_utente

    print(f"Nome utente o password sbagliata")
    return False, ""


def classifica(users):
    """
    Stampa la classifica degli utenti in base al punteggio.
    """
    # Ordina la classifica in base al punteggio (decrescente)
    classifica_users = sorted(users.items(), key=lambda item: item[1]["punteggio"], reverse=True)

    # Stampa la classifica
    for index, (id_user, user) in enumerate(classifica_users, start=1):
        print(f"{index}° posto: {user['nome']} -> {user['punteggio']}")


def registra_user(users):
    """
    Registra un nuovo utente, evitando duplicati.
    """
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")

    # Controlla se l'utente è già registrato
    for id_user, dati in users.items():
        if dati["nome"] == nome:
            print("Utente già registrato.")
            return

    # Registra un nuovo utente
    id_user = len(users) + 1
    users[id_user] = {"nome": nome, "password": password, "punteggio": 0}
    print(f"Registrazione completata per {nome} con ID utente {id_user}")


def main(users):
    """
    Funzione principale: gestisce registrazione, login e accesso ai giochi.
    """
    while True:
        scegli = input(
            "Inserisci 'registra' per registrarti, 'login' per loggarti o 'esci' per terminare: "
        ).lower()

        if scegli == "registra":
            registra_user(users)
        elif scegli == "esci":
            break
        elif scegli == "login":
            result, nome = login(users)
            if result:
                punteggio = menu_giochi(nome)
                if punteggio is not None:
                    # Aggiorna il punteggio dell'utente
                    for id_user, dati in users.items():
                        if dati["nome"] == nome:
                            dati["punteggio"] += punteggio

                    # Mostra la classifica
                    choice = input("Vuoi stampare la classifica? (Y/N): ").lower()
                    if choice in {"y", "yes"}:
                        classifica(users)
        else:
            print("Scelta non valida. Riprova.")


# Avvio del programma
users = {}
main(users)

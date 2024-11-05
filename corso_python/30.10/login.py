
#main del login
def login():
    scelta = input("Sei un admin o un user? ").lower()
    if scelta == "a" or scelta == "admin":
        login_admin()
    elif scelta == "u" or scelta == "user":
        login_user()


#main della registrazione
def registrazione():
    scelta = input("Sei un admin o un user? ").lower()
    if scelta == "a" or scelta == "admin":
        registrazione_admin()
    elif scelta == "u" or scelta == "user":
        registrazione_user()


#login per gli user
def login_user():
    username = input("Inserisci il nome user: ").lower()
    if username in users.keys():
        password = input("Inserisci la password: ").lower()
        if password == users[username]:
            print("Login effettuato con successo")
            funzione_user()
    else:
        print("User non trovato")


#login per gli admin
def login_admin():
    username = input("Inserisci il nome admin: ").lower()
    if username in admins.keys():
        password = input("Inserisci la password: ").lower()
        if password == admins[username]:
            print("Login effettuato con successo")
            funzione_admin()
    else:
        print("Admin non trovato")


#registrazione degli user
def registrazione_user():
    username = input("Inserisci il nome user: ").lower()
    if username in users.keys():
        password = input("User già presente, inserisci la password: ").lower()
        if password == users[username]:
            print("Login effettuato con successo")
            funzione_user()
    else:
        password = input("Inserisci la password: ").lower()
        users[username] = password
        print("Benvenuto", username, "la tua password è: ", password)
        funzione_user()


#registrazione degli admin
def registrazione_admin():
    username = input("Inserisci il nome admin: ").lower()
    if username in admins.keys():
        password = input("Admin già presente, inserisci la password: ").lower()
        if password == admins[username]:
            print("Login effettuato con successo")
            funzione_admin()
    else:
        password = input("Inserisci la password: ").lower()
        admins[username] = password
        print("Benvenuto", username, "la tua password è: ", password)
        funzione_admin()


#funzioni relativa agli admin
def richiesta():
    n=int(input("Dammi un numero: "))

    return n


def fibonacci(n):
    fibonacci=[0,1]

    if n == 0:
        print(fibonacci[0])
        
    elif n == 1:
        print(fibonacci)

    else:
        f=0
        while True:
            f=fibonacci[-1]+fibonacci[-2]
            if f<n:
                fibonacci.append(f)
            else:
                break

    print(fibonacci)         

#la funzione admin genera la successione di fibonacci da 0 a n inserito
def funzione_admin():
    n=richiesta()
    fibonacci(n)


#funzione che prende in input un numero n e conta all'indietro fino a 0
def funzione_user():
    n = int(input("Dammi un numero: "))
    for i in range(n,-1,-1):
        print(i)


users = {
    
}

admins = {

}

choice = True
while choice: 

    if len(admins) == 0 and len(users) == 0:
        registrazione()
    else:
        scelta_iniziale = input("Vuoi fare il login o registrarti? (L \\ R) \n(Per uscire scrivere esc) ").lower()

        if scelta_iniziale == "l":
            login()
        elif scelta_iniziale == "r":
            registrazione()
        elif scelta_iniziale == "esc" or scelta_iniziale == "e":
            choice = False
        else:
            print("Scelta non disponibile")
        


from modulo_menu import Menu, Elemento, Azione
from modulo_login import Utente, SistemaLogin


# Definizione delle azioni di esempio


def registrazione():
    username = input("Inserisci l'username: ").lower()
    if not sistema_login.controlla_utente(username):
        password = input("Inserisci una password: ").lower()
        domanda_segreta = input("Qual era il nome della tua scuola elementare?: ").lower()
        sistema_login.crea_nuovo_utente(username, password, domanda_segreta)
    else:
        print("Utente già registrato.")


def effettua_login():
    username = input("Inserisci l'username: ")
    if sistema_login.controlla_utente(username):
        password = input("Inserisci la password: ")
        check = sistema_login.effettua_login(username, password)
        if check:
            menulogin.mostra_menu()

    else:
        print("Utente non trovato.")


def reset_password():
    username = input("Inserisci l'username: ")
    if sistema_login.controlla_utente(username):
        sistema_login.reset_password(username)
    else:
        print("Utente non trovato.")



# Initialzza sistemi e menu
sistema_login = SistemaLogin()
menu_iniziale = Menu()
menulogin = Menu()

# Costruzione del menù iniziale
menu_iniziale.aggiungi_elemento(Elemento("Registrazione", Azione(registrazione)))
menu_iniziale.aggiungi_elemento(Elemento("Login", Azione(effettua_login)))
menu_iniziale.aggiungi_elemento(Elemento("Reimposta Password", Azione(reset_password)))

# Costruzione del menù dopo il login
elemento1_menulogin = Elemento("MENU LOGIN")
elemento2_menulogin = Elemento("Prova")
elemento3_menulogin = Elemento("Prova")

# Mostra il menù iniziale
menu_iniziale.mostra_menu()

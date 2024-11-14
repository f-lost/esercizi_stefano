from modulo_menu import Menu, Elemento, Azione
from modulo_login import Utente, SistemaLogin
import mysql.connector
import hashlib



#query = "select * from voti join studenti on voti.id = studenti.id where studenti.id in select utenti.id from studenti join utenti on studenti.id = utenti.id where utenti.username = " + username
# Definizione delle azioni

#FUNZIONI GENERALI
def registrazione():
    username = input("Inserisci l'username: ").lower()
    query = "select id from utenti where username = %s"
    mycursor.execute(query, username)
    utente = mycursor.fetchone()

    if utente:

        print("Utente già registrato.")

    else:

        nome = input("Inserisci il nome dello studente: ").lower()
        cognome = input("Inserisci il cognome dello studente: ").lower()
        valore = (nome, cognome)
        query = "select id from studenti where nome = %s and cognome = %s"
        mycursor.execute(query, valore)
        studente = mycursor.fetchone()

        if studente:

            print(f"Studente associato a {username} già esistente.")

        else:

            query = "insert into studenti (nome, cognome) values (%s, %s)"
            mycursor.execute(query, valore)
            mydb.commit()
            query = "select id from studenti where nome = %s and cognome = %s"
            mycursor.execute(query, valore)
            mydb.commit()
            studente = mycursor.fetchone()

            print(f"Studente {nome} {cognome} inserito.")
            password = input("Inserisci una password: ").lower()
            password_criptata = hashlib.md5(password.encode()).hexdigest()
            query = "insert into utenti (id, username, password, isadmin) values (%s, %s, %s, %s)"
            valori = (studente[0], username, password, 0)
            mycursor.execute(query, valori)
            mydb.commit()
 
def effettua_login():
    username = input("Inserisci l'username: ").lower()
    query = "select id from utenti where username = %s"
    mycursor.execute(query, username)
    utente = mycursor.fetchone()

    if utente:

        password = input("Inserisci la password: ").lower()
        password_criptata = hashlib.md5(password.encode()).hexdigest()
        query = "select password from utenti where username = %s"
        mycursor.execute(query, username)
        password_salvata = mycursor.fetchone()
        if password_criptata == password_salvata:
            print("Login effettuato con successo!")
            query = "select isadmin from utenti where username = %s"
            mycursor.execute(query, username)
            isadmin = mycursor.fetchone()

            if isadmin:

                menu_admin.mostra_menu()

            else:

                menu_utente.mostra_menu()


        else:

            print("Password errata. Riprovare.")

    else:

        print("Utente non trovato.")

#FUNZIONI PER ADMIN
def inserisci_studente_utente():

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    id_studente = mycursor.fetchone()
    if id_studente:
       print("Studente già esistente.")
    else:
        username = cognome[:4] + nome[:4]
        password = password = username[0] + "1" + username[2] + "2" + username[4] + "3" + username[6] + "4"
        password_criptata = hashlib.md5(password.encode()).hexdigest()
        query = "insert into studenti (nome, cognome) values (%s, %s)"
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Studente {nome} {cognome} inserito.")

        query = "select id from studenti where nome = %s and cognome = %s"
        mycursor.execute(query, valore)
        mydb.commit()
        id_studente = mycursor.fetchone() 

        query = "insert into utenti (id, username, password, isadmin) values (%s, %s, %s, %s)"
        valore = (id_studente[0], username, password_criptata, 0)
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Utente {username} inserito.")

def elimina_studente():

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    id_studente = mycursor.fetchone()
    if id_studente:
        query ="select username from utenti where id = %s"
        mycursor.execute(query, id_studente)
        username = mycursor.fetchone()
        query = "delete from studenti where nome = %s and cognome = %s "
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Studente {nome} {cognome} eliminato.")
        print(f"Utente {username} eliminato.")
    else:
        print("Studente non trovato.")

def rendi_admin():
    username = input("Inserisci username: ")
    query = "update utenti set isadmin = true where utenti.id = select utenti.id from utenti join studenti on utenti.id = studenti.id where utenti.username = %s"
    mycursor.execute(query, username)

def modifica_voto():

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        materia = input("Inserisci la materia: ").lower()
        voto = float(input("Inserisci il voto: "))
        valore = (materia, voto, studente[0])
        query = "insert into voti (materia, voto, id) values (%s, %s, %s)"
        mycursor.execute(query, valore)
        mydb.commit()
        print("Voto inserito.")
    else:
        print("Studente non trovato.")

def stampa_studenti():

    #query = "SELECT CASE WHEN ( (SELECT isadmin from utenti) not false ) THEN select studenti.nome, studenti.cognome, voti.materia, voti.voto from studenti join voti on studenti.id = voti.id ELSE select 1 from dual where false END"
    query = "select studenti.nome, studenti.cognome, voti.materia, voti.voto from studenti join voti on studenti.id = voti.id"
    mycursor.execute(query)
    risultati = mycursor.fetchall()
    for riga in risultati:
        print(riga)

def stampa_utenti():

    #query = "SELECT CASE WHEN ( (SELECT isadmin from utenti) not false ) THEN select studenti.nome, studenti.cognome, voti.materia, voti.voto from studenti join voti on studenti.id = voti.id ELSE select 1 from dual where false END"
    query = "select username, nome, cognome, isadmin from utenti join studenti on utenti.id = studenti.id"
    mycursor.execute(query)
    risultati = mycursor.fetchall()
    for riga in risultati:
        print(riga)

def media():

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        id = studente[0]
        materia = input("Inserisci la materia: ").lower()
        query = "select voto from voti where id = %s and materia = %s"
        mycursor.execute(query, (id, materia))
        voti = mycursor.fetchall()
        if voti:
            media_voti = round(sum(v[0] for v in voti) / len(voti), 2)
            print(f"La media di {nome} {cognome} in {materia} è: {media_voti}.")
        else:
            print("Nessun voto trovato per questa materia.")
    else:
        print("Studente non trovato.")

#FUNZIONI PER UTENTI NON ADMIN
def media():

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        id = studente[0]
        materia = input("Inserisci la materia: ").lower()
        query = "select voto from voti where id = %s and materia = %s"
        mycursor.execute(query, (id, materia))
        voti = mycursor.fetchall()
        if voti:
            media_voti = round(sum(v[0] for v in voti) / len(voti), 2)
            print(f"La media di {nome} {cognome} in {materia} è: {media_voti}.")
        else:
            print("Nessun voto trovato per questa materia.")
    else:
        print("Studente non trovato.")



#CREAZIONE DEL DATABASE E DELLA TABELLA
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root"
)

mycursor = mydb.cursor()
query = "create database if not exists Registro"
mycursor.execute(query)

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root",
database = "Registro"
)

mycursor = mydb.cursor()
query = "create table if not exists studenti (id int auto_increment primary key, nome varchar(50), cognome varchar(50))"
mycursor.execute(query)

query = "create table if not exists voti (id_voti auto_increment primary key, id int, materia varchar(50), voto float, foreign key (id) references studenti(id) on delete cascade)"
mycursor.execute(query)

query = "create table if not exists utenti (id_utenti auto_increment primary key, id int, username varchar(50), password varchar(50), isadmin bool, foreign key (id) references studenti(id) on delete cascade)"
mycursor.execute(query)


# Initialzza sistemi e menu
sistema_login = SistemaLogin()
menu_iniziale = Menu()

# Costruzione del menù iniziale
menu_iniziale.aggiungi_elemento(Elemento("Registrazione", Azione(registrazione)))
menu_iniziale.aggiungi_elemento(Elemento("Login", Azione(effettua_login)))

# Costruzione del menù dopo il login

menu_admin = Menu()
elemento1_admin = Elemento("Inserisci Studente", Azione(inserisci_studente_utente))
elemento2_admin = Elemento("Elimina Studente", Azione(elimina_studente))
elemento3_admin = Elemento("Inserisci Voto", Azione(modifica_voto))
elemento4_admin = Elemento("Calcola Media", Azione(media))
elemento5_admin = Elemento("Stampa Registro Studenti", Azione(stampa_studenti))
elemento6_admin = Elemento("Stampa Registro Utentu", Azione(stampa_utenti))
elemento7_admin = Elemento("Rendi Admin", Azione(rendi_admin))

menu_admin.aggiungi_elemento(elemento1_admin)
menu_admin.aggiungi_elemento(elemento2_admin)
menu_admin.aggiungi_elemento(elemento3_admin)
menu_admin.aggiungi_elemento(elemento4_admin)
menu_admin.aggiungi_elemento(elemento5_admin)
menu_admin.aggiungi_elemento(elemento6_admin)
menu_admin.aggiungi_elemento(elemento7_admin)



menu_utente = Menu()
elemento1_utente = Elemento("Calcola Media", Azione(media_utente))
elemento2_utente = Elemento("Stampa Registro", Azione(stampa_voti_studente))

# Mostra il menù iniziale
menu_iniziale.mostra_menu()
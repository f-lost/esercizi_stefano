from modulo_menu import Menu, Elemento, Azione
import mysql.connector


# Definizione delle azioni di esempio
def inserisci_studente():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    valore = (nome, cognome)
    query = "insert into studenti (nome, cognome) values (%s, %s)"
    mycursor.execute(query, valore)
    mydb.commit()
    print(mycursor.rowcount, "Studenti inseriti")

       
def elimina_studente():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    valore = (nome, cognome)
    query = "delete from studenti where nome = %s and cognome = %s  "
    mycursor.execute(query, valore)
    mydb.commit()
    print(mycursor.rowcount, "Studenti eliminati")


def modifica_voto():

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    query = "select nome, cognome from studenti"
    mycursor.execute(query)
    all_studenti = mycursor.fetchall()
    if (nome,cognome) in all_studenti:
        query = f"select id from studenti where nome = {nome} and cognome = {cognome}"
        mycursor.execute(query)
        id = mycursor.fetchone()
        materia = input("Inserisci la materia").lower()
        voto = float(input("Inserisci il voto: "))
        valore = (materia, voto, id[0])
        query = "update voti set materia = %s, voto = %s, id = %s"
        mycursor.execute(query, valore)
        mydb.commit()
        print(mycursor.rowcount, "Voti modificati")

def stampa():

    query = "select * from studenti join voti on studenti.id = voti.id"
    mycursor.execute(query)
    risultati = mycursor.fetchall()
    for riga in risultati:
        print(riga)

def media():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    query = "select nome, cognome from studenti"
    mycursor.execute(query)
    all_studenti = mycursor.fetchall()
    if (nome,cognome) in all_studenti:
        query = f"select id from studenti where nome = {nome} and cognome = {cognome}"
        mycursor.execute(query)
        id = mycursor.fetchone()
        materia = input("Inserisci la materia: ")
        query = "select materia from voti"
        mycursor.execute(query)
        all_materie = mycursor.fetchall()
        if (materia) in all_materie:
            query = f"select {materia} from voti where id = {id[0]}"
            mycursor.execute(query)
            voti = mycursor.fetchone()
            media = (sum(voti))/len(voti)
            print(f"La media dello studente {nome} {cognome} è: {media}")


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

query = "create table voti (materia varchar(50), voto float, id int foreign key references studenti(id))"
mycursor.execute(query)



# Creazione del menu e aggiunta degli elementi
menu = Menu()

elemento1 = Elemento("Inserisci Studente", Azione(inserisci_studente))
elemento2 = Elemento("Inserisci Voto", Azione(modifica_voto))
elemento3 = Elemento("Elimina Studente", Azione(elimina_studente))
elemento4 = Elemento("Calcola Media", Azione(media))
elemento5 = Elemento("Stampa Registro", Azione(stampa))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)
menu.aggiungi_elemento(elemento4)
menu.aggiungi_elemento(elemento5)

# Mostra il menu ripetibile
menu.mostra_menu()

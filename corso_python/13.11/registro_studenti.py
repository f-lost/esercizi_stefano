from modulo_menu import Menu, Elemento, Azione
import mysql.connector


# Definizione delle azioni di esempio
def inserisci_studente():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    italiano = 0
    matematica = 0
    valore = (nome, cognome, italiano, matematica)
    query = "insert into studenti (nome, cognome, italiano, matematica) values (%s, %s, %s, %s)"
    mycursor.execute(query, valore)
    mydb.commit()

       
def elimina_studente():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    valore = (nome, cognome)
    query = "delete from studenti where nome = %s and cognome = %s  "
    mycursor.execute(query, valore)
    mydb.commit()


def modifica_voto():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    italiano = int(input("Inserisci un voto per italiano: "))
    matematica = int(input("Inserisci un voto per matematica: "))
    valore = (italiano, matematica, nome, cognome)
    query = "update studenti set italiano = %s, matematica = %s where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    mydb.commit()

def stampa():

    query = "select * from studenti"
    mycursor.execute(query)
    risultati = mycursor.fetchall()
    for riga in risultati:
        print(riga)

def media():

    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    valore = (nome, cognome)
    query = "select italiano, matematica from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    voti = mycursor.fetchone()
    italiano = voti[0]
    matematica = voti[1]
    media = (italiano + matematica)/2
    print(f"La media dello studente {nome} {cognome} è: {media}")


#CREAZIONE DEL DATABASE E DELLA TABELLA
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root"
)

mycursor = mydb.cursor()
query = "create database if not exists studenti"
mycursor.execute(query)

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  database = "studenti"
)

mycursor = mydb.cursor()
query = "create table if not exists studenti (id int auto_increment primary key, nome varchar(50), cognome varchar(50), italiano int, matematica int)"
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

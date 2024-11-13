from modulo_menu import Menu, Elemento, Azione
import mysql.connector


# Definizione delle azioni
def inserisci_studente():

#VECCHIO
    # nome = input("Inserisci il nome dello studente: ")
    # cognome = input("Inserisci il cognome dello studente: ")
    # valore = (nome, cognome)
    # query = "insert into studenti (nome, cognome) values (%s, %s)"
    # mycursor.execute(query, valore)
    # mydb.commit()
    # print(mycursor.rowcount, "Studenti inseriti")

#MODIFICATO
    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
       print("Studente già esistente.")
    else:
        query = "insert into studenti (nome, cognome) values (%s, %s)"
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Studente {nome} {cognome} inserito.")

def elimina_studente():

#VECCHIO
    # nome = input("Inserisci il nome dello studente: ")
    # cognome = input("Inserisci il cognome dello studente: ")
    # valore = (nome, cognome)
    # query = "delete from studenti where nome = %s and cognome = %s  "
    # mycursor.execute(query, valore)
    # mydb.commit()
    # print(mycursor.rowcount, "Studenti eliminati")

#MODIFICATO

    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        query = "delete from studenti where nome = %s and cognome = %s  "
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Studente {nome} {cognome} eliminato.")
    else:
        print("Studente non trovato.")


def modifica_voto():
#VECCHIO
    # nome = input("Inserisci il nome dello studente: ").lower()
    # cognome = input("Inserisci il cognome dello studente: ").lower()
    # query = "select nome, cognome from studenti"
    # mycursor.execute(query)
    # all_studenti = mycursor.fetchall()
    # if (nome,cognome) in all_studenti:
    #     query = f"select id from studenti where nome = {nome} and cognome = {cognome}"
    #     mycursor.execute(query)
    #     id = mycursor.fetchone()
    #     materia = input("Inserisci la materia").lower()
    #     voto = float(input("Inserisci il voto: "))
    #     valore = (materia, voto, id[0])
    #     query = "update voti set materia = %s, voto = %s, id = %s"
    #     mycursor.execute(query, valore)
    #     mydb.commit()
    #     print(mycursor.rowcount, "Voti modificati")

#MODIFICATO
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

def stampa():
#VECCHIO
    # query = "select * from studenti join voti on studenti.id = voti.id"
    # mycursor.execute(query)
    # risultati = mycursor.fetchall()
    # for riga in risultati:
    #     print(riga)
#MODIFICATO
    query = "select studenti.nome, studenti.cognome, voti.materia, voti.voto from studenti join voti on studenti.id = voti.id"
    mycursor.execute(query)
    risultati = mycursor.fetchall()
    for riga in risultati:
        print(riga)

def media():
#VECCHIA
    # nome = input("Inserisci il nome dello studente: ")
    # cognome = input("Inserisci il cognome dello studente: ")
    # query = "select nome, cognome from studenti"
    # mycursor.execute(query)
    # all_studenti = mycursor.fetchall()
    # if (nome,cognome) in all_studenti:
    #     query = f"select id from studenti where nome = {nome} and cognome = {cognome}"
    #     mycursor.execute(query)
    #     id = mycursor.fetchone()
    #     materia = input("Inserisci la materia: ")
    #     query = "select materia from voti"
    #     mycursor.execute(query)
    #     all_materie = mycursor.fetchall()
    #     if (materia) in all_materie:
    #         query = f"select {materia} from voti where id = {id[0]}"
    #         mycursor.execute(query)
    #         voti = mycursor.fetchone()
    #         media = (sum(voti))/len(voti)
    #         print(f"La media dello studente {nome} {cognome} è: {media}")
#MODIFICATO
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
            media_voti = sum(v[0] for v in voti) / len(voti)
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

#query = "create table voti (materia varchar(50), voto float, id int foreign key references studenti(id))" 
#modificato in
query = "create table voti (id int, materia varchar(50), voto float, foreign key (id) references studenti(id) on delete cascade)"
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

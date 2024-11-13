import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )

# mycursor = mydb.cursor()

# # query = "create database pythonmysql"
# query = "show databases"

# mycursor.execute(query)

# for x in mycursor:
#     print(x)

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  database = "pythonmysql"
)

#query = "create table utenti (id int auto_increment primary key, nome varchar(50), indirizzo varchar(50))"
def inserimento():
    query = "insert into utenti (nome, indirizzo) values (%s, %s)"

    #valori = ("stefano", "via roma")
    valori = [("tommaso","via milano"),
            ("simone","via bari"),
            ("renato","via torre")]

    mycursor.executemany(query, valori)

    mydb.commit()

    print("Record inseriti: " ,mycursor.rowcount)

# mycursor = mydb.cursor()

# query = "select * from utenti where nome = %s"
# valore = ("simone",)

# mycursor.execute(query, valore)

# risultati = mycursor.fetchall()

# print(risultati)

# for riga in risultati:
    
#     print(riga)


mycursor = mydb.cursor()

query = "delete from utenti where nome = %s"

valore = ("simone",)

mycursor.execute(query, valore)

mydb.commit()

print(mycursor.rowcount, "record eliminati")
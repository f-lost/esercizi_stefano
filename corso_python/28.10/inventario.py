#Esercizio Gestione Negozio
admin=("admin","password") #unico admin
user=("pippo","pluto") #unico utente preesistente

inventario={
  "pane": 2,
  "latte": 1.50,
  "uova": 2.50
}

acquisti=[]

choice=input("Digita R per registrarti o L per fare il login: ").lower()
#login e registrazione
if (choice == "r"):
  username=input("Inserisci il tuo username: ")
  password=input("Inserisci la tua password: ")
  nuovo_utente=(username, password)
  scelta=int(input("Cosa vuoi fare?\n 1)Visualizza inventario.\n 2)Acquista merce.\n 3)Visualizza lista acquisti\n:"))
  if (scelta == 1):
    print(inventario)
  elif (scelta == 2):
    elem=input("Quale elemento vuoi comprare?\n")

    if (inventario.get(elem) == None):
      print("Elemento non trovato")
    else:
      acquisti.append(elem)
      print("La tua lista degli acquisti è la seguente:\n", acquisti)
  elif (scelta == 3):
    print("Visualizza lista acquisti:\n", acquisti)
  else:
    print("Scelta non valida")
    
elif (choice == "l"):
  
  username_input=input("Inserisci il tuo username: ")
  if (username_input == "admin"):
    password_input=input("ADMIN: Inserisci la tua password: ")
    if (password_input == "password"):
      print("Login effettuato")
      scelta=int(input("Cosa vuoi fare?\n 1)Visualizza inventario.\n 2)Modifica inventario.\n 3)Cancella elemento\n:"))
      if (scelta == 1):
        print(inventario)
      elif (scelta == 2):
        print("Modifica inventario:\n")
        x=input("Quale elemento dell'inventario vuoi modificare?").lower()
        if (inventario.get(x) == None):
          y=input("Inserisci il nuovo elemento: ").lower()
          y_costo=input("Inserisci il costo: ")
          inventario[y]=x
        else:
          y_costo=input("Inserisci il nuovo costo: ")
          inventario[x]=y_costo

      elif (scelta == 3):
        x=input("Quale elemento dell'inventario vuoi cancellare?").lower()
        inventario.pop(x,"Elemento non presente")
      else:
        print("Scelta non valida")
    else:
      print("Password errata")
      
  elif (username_input == user[0]):
    password_input=input("Inserisci la tua password: ")
    if (password_input == user[1]):
      print("Login effettuato")
      scelta=int(input("Cosa vuoi fare?\n 1)Visualizza inventario.\n 2)Acquista merce.\n 3)Visualizza lista acquisti\n:"))
      if (scelta == 1):
        print(inventario)
      elif (scelta == 2):
        x=input("Quale elemento vuoi comprare?\n")
        
        if (inventario.get(x) == None):
          print("Elemento non trovato")
        else:
          acquisti.append(x)
          inventario.pop(x)
          print("La tua lista degli acquisti è la seguente:\n, acquisti")
          
      elif (scelta == 3):
        print("Visualizza lista acquisti:\n", acquisti)
      else:
        print("Scelta non valida")
    else:
      print("Password errata")
  else:
    print("Utente non trovato")

else:
  print("Scelta non valida")
# eta  = 27
# patente = "si"
# tasso_alcol= "alto"

# if eta < 18:
#     print("Non puoi guidare perchè sei minorenne")
# elif patente != "si":
#     print("Non puoi guidare perchè non hai la patente")
# elif tasso_alcol != "basso":
#     print ("Non puoi guidare perchè hai bevuto")
# else:
#     print("Puoi guidare")



# if eta < 18 or patente != "si" or tasso_alcol != "basso":
#     print("Non puoi guidare")
# else:
#     print("Puoi guidare")

# if eta < 18: print("Non puoi guidare perchè sei minorenne")
# elif patente != "si": print("Non puoi guidare perchè non hai la patente")
# elif tasso_alcol != "basso": print ("Non puoi guidare perchè hai bevuto")
# else: print("Puoi guidare")


# print("non puoi guidare perchè sei minorenne" if eta < 18 else "puoi guidare")

# # o anche 

# esito = "non puoi guidare perchè sei minorenne" if eta < 18 else "puoi guidare"

# count = 0


##############################################################################################################


# while count < 10:
#     count += 1
#     if count == 5:
#         print("ops")
#         print("giro saltato")
#         continue
#     print(count)
#     print("giro regolare")


##############################################################################################################



# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# lista2 = lista[0:15:5]

# print(lista2)

# numero = input("Inserisci un numero: ")

# if numero.isdecimal():
#     print("è un numero convertibile")
# else:
#     print("numero non convertibile")

# stringa = input("dammi una stringa")

# print(stringa.isalpha()) #"isspace" "isnum?"

# stringa = "ciao a tutti"

# print(stringa.count("t"))


# lista = ["ciao", "a" ,"tutti"]


# stringa = "ciao a tutti"

# print("ci" in stringa)


# frutta =["mela", "pera", "uva", "arancia"]

# fruttaE = [frutto for frutto in frutta if "e" in frutto]

# print(fruttaE)


##############################################################################################################

# parola = input("Inserisci una parola: ")
# vocali = "aeiou"
# res=" "
# for i, c in enumerate(parola):
#     if c in vocali:
#         res += c+str(i) + " "
# print(res)


##############################################################################################################

# while True:
#     frase = input("Inserisci una stringa: ").lower()

#     caratteri = set(frase)

#     frequenza = { }

#     for carattere in caratteri:
#         frequenza[carattere] = frase.count(carattere)

#     frequenza = dict(sorted(frequenza.items()))
#     print(frequenza)

#     scelta = input("Vuoi uscire? (Y\\N): ").lower()

#     if scelta != "n":
#         break



##############################################################################################################

# def media(classe):

#     for alunno in classe:
#         media = sum(classe[alunno])/len(classe[alunno])
#         print("Nome: ", alunno , " Media: ", media)
        

# def nuovovoto(classe):

#     alunno = input("Scrivi il nome dell'alunno: ").lower()
#     voto = int(input("Scrivi il voto: "))

#     if alunno not in classe:
#         classe[alunno] = []
    
#     classe[alunno].append(voto)



# classe={ }


# while True:
#     choice = input("Digita \"voto\" per inserire un nuovo voto, digita \"media\" per stampare la media dei voti di tutta la classe: ").lower()
    
#     if choice == "voto":
#         nuovovoto(classe)

#     elif choice == "media":
#         media(classe)    
    
#     else:
#         print("Scelta non valida")


#     scelta = input("Vuoi uscire? (Y\\N): ").lower()

#     if scelta != "n":
#         break



##############################################################################################################



# lista = [1,2,3,4,5]
# lista_pari = [ num for num in lista if num % 2 == 0]

# print(lista_pari)

# dizionario = { (key, value) for key, value in dict.items()}

# dict1 = { "a": 1, "b":2, "c":3 }

# dizionario = {k:v*2 for k,v in dict1.items()}

# print(dizionario)

#######################################   ARGOMENTI MULTIPLI PER FUNZIONE   ############################################################


#esempio di funzione quando non so il numero di argomenti


# def funzione(*argomenti):
#     print(type(argomenti))
#     print(argomenti)
#     for arg in argomenti:
#         print(arg)

# def funzione2(**arg):
#     print(type(arg))


# funzione(11,2,4)

# funzione2(num1 = 11, num2 = 4, num3 = 3)

########################################   VARIABIL GLOBALI   ##################################################

#cambiare valori variabile globale

# variabile1 = 10 

# def funzione():
#     global variabile1
#     variabile1 += 1

# print(variabile1)
# funzione()
# print(variabile1)
# funzione()
# print(variabile1)
# funzione()
# print(variabile1)


##############################################################################################################

# def triplica(a):

#     return a*3

# lista = [1,2,3,4,5]


# listaT = []

# for num in lista:
#     listaT.append(triplica(num))

# print(listaT)


#####################################   FUNZIONE MAP   ########################################################

# def triplica(a):

#     return a*3

# lista = [1,2,3,4,5]

# listaT = list(map(triplica, lista))
# print(listaT)


################################################################################################################

# lista = [1,2,3,4,5]


# def numero_p(n):
#     return n%2 == 0

# listaP = list(filter(numero_p, lista))

# print(listaP)

################################################################################################################

def eliminapunteggiatura(stringa):          #SBAGLIATO,POTEVO USARE .isalnum()
         
    punteggiatura = [" ", ",", ".", ";", ":", "_", "-","!","?"]  
    
    for elem in punteggiatura:
        stringa = stringa.replace(elem, "")

    return stringa

def palindroma(stringa):                #SBAGLIATO,POTEVO DIRETTAMENTE FARE if stringa == stringa[::-1]
    
    if len(stringa)%2 != 0:
        
        meta = len(stringa)//2
        stringa = stringa[:meta] + stringa[meta + 1:]
        prima_meta_stringa = stringa[:meta]
        seconda_meta_stringa = stringa[meta:]
        seconda_meta_stringa = seconda_meta_stringa[::-1]

    else:
        
        meta = len(stringa)//2
        prima_meta_stringa = stringa[:meta]
        seconda_meta_stringa = stringa[meta:]
        seconda_meta_stringa = seconda_meta_stringa[::-1]

    if prima_meta_stringa == seconda_meta_stringa:
        print("La frase è palindroma")
    else:
        print("la frase non è palindroma")



stringa = input("Scrivi una frase: ").lower()

stringa = eliminapunteggiatura(stringa)

palindroma(stringa)
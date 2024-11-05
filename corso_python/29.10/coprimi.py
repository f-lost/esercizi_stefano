

#calcolo i fattori si un numero
def calcola_fattori(x):
    fattori=[]
    for i in range(1,x+1):
        if x % i == 0:
            fattori.append(i)
    return fattori


choice = True 

scelta_iniziale=int(input("Vuoi controllare due numeri o due stringhe? Digita 1 per i numeri, 2 per le stringhe: "))

if scelta_iniziale == 1:
    while choice:
        print("Inserisci due numeri di cui vuoi controllare i fattori comuni\n")
        a=int(input("Inserisci il primo numero: "))
        b=int(input("Inserisci il secondo numero: "))

        #calcolo i fattori di a e b e li casto come insiemi
        fattori_a=set(calcola_fattori(a))
        fattori_b=set(calcola_fattori(b))

        #faccio l'intersezione dei fattori per trovare quelli comuni
        fattori_comuni=list(fattori_a & fattori_b)

        #se c'è più di 1 come fattore comune i numeri non sono coprimi
        if len(fattori_comuni) > 1:
            print("I fattori comuni sono: ", fattori_comuni)
        else:
            print("I numeri sono coprimi")

        ripeti=input("Vuoi ripetere con un nuovo numero? (Y/N): ").lower()

        if ripeti == "n" or ripeti == "no":
            #se l'utente non vuole continuare si esce dal while
            choice = False
elif scelta_iniziale == 2:
    print("Inserisci le due stringhe che vuoi controllare\n")
    a=set(input("Inserisci la prima stringa: "))
    b=set(input("Inserisci la seconda stringa: "))

    #troviamo le lettere comuni

    lettere_comuni= a & b

    


else:
    print("Scelta non valida")
        


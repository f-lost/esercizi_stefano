#funzione che prende in input un numero e stampa Pari se è pari Dispari se è dispari
def paridispari(n):
    if n % 2 == 0:
        print("Pari")
    else:
        print("Dispari")

#funzione che prende in input un numero n e conta all'indietro fino a 0
def containdietro(n):
    for i in range(n,-1,-1):
        print(i)

#funzione che prende in input una lista e stampa il quadrato di ogni elemento
def quadrati(lista):
    for i in lista:
        print(i ** 2)

#funzione che prende in input una lista e ne trova il massimo
def massimo(lista):
    m = lista[0]
    for i in lista:
        if i>=m :
            m=i
    return m

#funzione che prende in input una lista e ne trova il massimo senza ciclo for
def massimo2(lista):
    lista=lista.sort()

    return lista[-1]


#funzione che trova quanti numeri diversi ci sono in una lista e li salva in una seconda lista (SENZA WHILE)
def numeri(lista):
    lista_senza_ripetizioni=set(lista)
    n=len(lista)
    return [n, lista_senza_ripetizioni]

def numeri2(lista):
    i=0
    lista_senza_ripetizioni=[]
    n=len(lista)
    while  i<n:
        pass


        




#main con ciclo infinito
uscita = True

while uscita:
    print("Quale funzione vuoi usare?\n 1) funzione che prende in input un numero e stampa Pari se è pari Dispari se è dispari \n2)funzione che prende in input un numero n e conta all'indietro fino a 0 \n3)funzione che prende in input una lista e stampa il quadrato di ogni elemento \n4)funzione per trovare il massimo di una lista che conta quanti numeri diversi ci sono in essa \nQualsiasi altra scelta farà uscire dal programma. ")
    choice = input(":")

    #stampa pari o dispari
    if choice == "1":
        n=int(input("Inserisci un numero: "))
        paridispari(n)

    #conta da n a 0
    elif choice == "2":
        n=int(input("Inserisci un numero: "))
        containdietro(n)

    ##il for serve per inserire in input la lista, poi stampa i quadrati degli elementi
    elif choice == "3":
        lista = []
        n = int(input("Inserisci il numero di elementi della lista: "))
        for i in range(n):
            elem = float(input())
            lista.append(elem)
        quadrati(lista)  

    #stampa Lista Vuota se la lista è vuota e salga in m il massimo e la lista final è: [numero di elementi diversi, [elementi diversi]]
    elif choice == "4":
        lista = []
        final = []
        n = int(input("Inserisci il numero di elementi della lista: "))
        for i in range(n):
            elem = int(input())
            lista.append(elem)
        if lista == []:
            print("Lista Vuota")
            break

        m=massimo(lista)
        final = numeri(lista)

        print("La lista ha ", final[0], " numeri diversi, che sono: ", final[1] , " e il massimo della lista è: ", m)


    else:
        uscita = False
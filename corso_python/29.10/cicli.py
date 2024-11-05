n = int(input("Inserisci un numero: "))
choice = True
primi=[]


while choice:
    #controlliamo se il numero è primo, presupponiamo sia primo
    p=1
    for i in range(2,n):
        if n % i == 0: 
            #se è divisibile per un numero da 2 a esso non è primo, diciamo all'utente e usciamo dal for            
            p=0 
            print("Il numero non è primo")
            break

    #se p rimane 1 il numero è primo
    if p == 1: 
        print("Il numero è primo")
        #salviamo i numeri primi in una lista
        primi.append(n) 

    #quando avremo 5 numeri primi usciamo dal while e stampiamoli    
    if len(primi) == 5: 
        print("Hai raggiunto 5 numeri primi:" ,primi)
        break

    #produciamo la stampa al contrario da n a 0 
    for i in range(n,-1,-1):
        print(i)
        
    #chiediamo all'utente se vuole riniziare con un nuovo numero
    ripeti=input("Vuoi ripetere con un nuovo numero? (Y/N): ").lower()

    if ripeti == "y" or ripeti == "yes":
        n = int(input("Inserisci un numero: "))
    else:
        #se l'utente non vuole continuare si esce dal while
        choice = False
        

# Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

# Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
# Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
# Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
# Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.



n=-1
while n < 0:
    n=int(input("Inserisci un numero positivo: "))


#creiamo una lista di numeri che va da 1 a n
numeri=[*(range(1,n+1))]
pari=[]
dispari=[]


#separiamo tutti i numeri primi da quelli dispari 
for i in numeri:
    if i%2 == 0:
        pari.append(i)
    else:
        dispari.append(i)
        
print(pari)
print(dispari)

somma_p=0
somma_d=0


for i in pari:
    somma_p += i
    # x = somma_p + i
    # somma_p = x
print("La somma di tutti i primi da 1 a ", n, " è: ", somma_p)


print("Stampo tutti i numeri dispari da 1 a ", n ,":")
for i in dispari:
    print(i)



#controlliamo se il numero è primo, presupponiamo sia primo
p=1
for i in range(2,n):
    if n % i == 0: 
        #se è divisibile per un numero da 2 a n non è primo, diciamo all'utente e usciamo dal for            
        p=0 
        print("Il numero non è primo")
        break

#se p rimane 1 il numero è primo
if p == 1: 
    print("Il numero è primo")
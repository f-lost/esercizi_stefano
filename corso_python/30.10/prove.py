dizionario = {

}

booleano = bool(input("Dammi un booleano: "))
intero = int(input("Dammi un intero: "))
stringa = input("Dammi una stringa: ")


lista=[booleano,intero,stringa]


dizionario["booleano"]=lista[0]
dizionario["intero"]=lista[1]
dizionario["stringa"]=lista[2]


print(dizionario)
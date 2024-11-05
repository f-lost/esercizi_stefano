# #esempi di incapsulamento


# class Computer:

#     def __init__(self):
#         self.__processore = "Intel i5" #Attributo privato

#     def get_processore(self):
#         return self.__processore
    
#     def set_processore(self, processore):
#         self.__processore = processore


# pc = Computer()

# print(pc.get_processore())

# pc.set_processore("AMD Ryzen 5")

# print(pc.get_processore())



#esempi di visibilità

numero = 10 #globale

def funzione_esterna():
    numero = 5 #locale nella funzione esterna

    def funzione_interna():
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()
    print("Numero dentro funzione_esterna (locale):", numero)

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)
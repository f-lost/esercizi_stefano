import numpy as np


class ArrayCasuale():

    def __init__(self,inizio : int, fine : int, quanti : int):

        self.array = np.random.randint(inizio, fine, size = quanti)

class ArraySlicer():

    def slice(self, array, inizio, fine, passo = 1):
        if inizio == ":":
            inizio = 0
        if fine == ":":
            fine = 0
        if fine < len(array.array):

            print(array.array[inizio : fine : passo])
            return array.array[inizio : fine : passo]
        else:
            print("ERRORE, slice più grande della dimensione dell'array")

    def modifica(self, array, inizio, fine, valore):

        if fine < len(array.array):
            array.array[inizio : fine] = valore
        else:
            print("ERRORE, slice più grande della dimensione dell'array")

    def stampa_array(self, array):

        print(array.array)




#test

# mainarray = ArraySlicing(10, 51, 20)

# mainarray.stampa()

# arr1 = mainarray.slicing(0, 11)
# arr2 = mainarray.slicing(-5, 50)
# arr3 = mainarray.slicing(5, 15)
# arr4 = mainarray.slicing(0 , 50 , 3)

# mainarray.modifica(5, 10, 99)

# mainarray.stampa_array(arr1)
# mainarray.stampa_array(arr2)
# mainarray.stampa_array(arr3)
# mainarray.stampa_array(arr4)


choice = True

while choice == True:

    print("Genererò un array unidimensionale di numeri casuali, dimmi il range (più piccolo/ più grande) e quanti ne vuoi.\n")
    inizio = int(input("Numero più piccolo: "))
    fine = int(input("Numero più piccolo: "))
    quanti = int(input("Quanti numeri casuali devo generare?: "))

    array = ArrayCasuale(inizio, fine, quanti)
    slicer = ArraySlicer()


    while True:

        scelta = int(input("Cosa vuoi fare?\n1)Slicing\n2)Modifica con un solo valore\n3)Stampa\n4)Nuovo array casuale\n5)Esci\n:  "))

        if scelta == 1:

            print("Inserisci inizio e fine della slice e il passo")
            inizio = int(input("Inizio: "))
            fine = int(input("Fine: "))
            passo = int(input("Passo: "))

            arr_1 = slicer.slice(array, inizio, fine, passo)

        elif scelta == 2:

            print("Inserisci inizio e fine della slice da modificare")
            inizio = int(input("Inizio: "))
            fine = int(input("Fine: "))
            valore = int(input("Inserisci il nuovo valore: "))

            slicer.modifica(array, inizio, fine, valore)


        elif scelta == 3:

            slicer.stampa_array(array)


        elif scelta == 4:

            break
        
        else:

            print("Ciao!")

            choice = False
            break
            







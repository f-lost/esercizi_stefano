import numpy as np


class Array():

    def __init__(self,inizio : int, fine : int, quanti : int):

        self.array = np.random.randint(inizio, fine, size = quanti)

    def slicing(self, inizio, fine, passo = 1):

        print(self.array[inizio : fine : passo])

        return self.array[inizio : fine : passo]

    def modifica(self, inizio, fine, valore):

        self.array[inizio : fine] = valore

    def stampa(self):

        print(self.array)

    def stampa_array(self, array):

        print(array)


mainarray = Array(10, 51, 20)

mainarray.stampa()

arr1 = mainarray.slicing(0, 11)

arr2 = mainarray.slicing(-5, 50)

arr3 = mainarray.slicing(5, 15)

arr4 = mainarray.slicing(0 , 50 , 3)


mainarray.modifica(5, 10, 99)

mainarray.stampa_array(arr1)
mainarray.stampa_array(arr2)
mainarray.stampa_array(arr3)
mainarray.stampa_array(arr4)









import numpy as np

class Array:

    def __init__(self):

        self.__array = np.arange(10, 50, 1)
    
    def __get_array(self):

        return self.__array
    
    def verifica(self):

        print("Tipo di dati:", self.__get_array().dtype)

    def cambia(self):

        self.__get_array().astype(np.float64)

    def stampa_forma(self):

        print("Forma dell'array:", self.__get_array().shape) 


#test

array = Array()

array.verifica()

array.cambia()

array.stampa_forma()
'''Create 2 array numpy:

- Un array unidimensionale di numeri casuali compresi tra 0 e 1;
- Un array bidimensionale di dimensione 3x3 con valori interi casuali.'''

import numpy as np
import random


n = int(input("Inserisci quanti elementi devo inserire nell'array: "))
array1d = np.random.rand(n)


array2d = np.random.randint(0,100, (3,3))

print(array1d)

print(array2d)



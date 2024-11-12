'''Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:

- Restituite la somma di tutti gli elementi dei singoli array che si trovano
 nell'ultima riga dalla seconda colonna in poi;
- Unite i 2 array secondo l'asse 1.

'''

import numpy as np

arr1 = np.random.randint(0,100, (4,4))
arr2 = np.random.randint(0,100,(4,4))

print(arr1)
print("")
print(arr2)

print("La somma degli elementi voluti del primo array è: ", np.sum(arr1[3:,1:]))
print("La somma degli elementi voluti del secondo array è: ", np.sum(arr2[3:,1:]))

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
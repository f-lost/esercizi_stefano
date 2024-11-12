'''
Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e 
fate i seguenti calcoli:

- Calcolo della media;
Calcolo della moda;
-Calcolo della deviazione standard;
- Trasformatelo in un array 5 X 10'''


import numpy as np
import scipy

arr = np.random.uniform(1, 1000, 50)


print(arr)

print("La media è: ", arr.mean())
moda = scipy.stats.mode(arr)
print("La moda è ", moda.mode, " con un conteggio di ",moda.count)
print("La deviazione standard è: ", np.std(arr))

arr_res = arr.reshape(5,10)

print(arr_res)


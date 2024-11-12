import numpy as np
import random
import pickle

dizionario = {"nome":"tommaso", "cognome":"muraca"}

# with open("prova2","wb") as file:
#     pickle.dump(dizionario, file)

with open("prova2", "rb") as file:
    contenuto = pickle.load(file)

print(contenuto)


elements = np.random.randint(0,100,(2,10))

x = np.std(elements)
print(elements)
print(x)


ages = [5, 31, 43, 17, 25, 47, 34, 55, 20, 19, 85, 75,77,70, 35, 56]

print(np.percentile(ages, 75))



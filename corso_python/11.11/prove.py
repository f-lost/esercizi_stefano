with open("prova.csv", "r") as file:
    contenuto = file.read()


righe = contenuto.split("\n")

righe = righe.split(",")

print(righe)
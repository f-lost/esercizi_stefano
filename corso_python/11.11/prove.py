with open("tabella.csv", "r") as file:
    contenuto = file.read()


righe = contenuto.split("\n")
for riga in righe[1:]:
    elementiRiga = riga.split(",")
    print(elementiRiga)

#righe = righe.split(",")

print(righe)
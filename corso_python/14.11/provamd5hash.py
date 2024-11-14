import hashlib


result = hashlib.md5("ciao".encode()).hexdigest()

print("prova",result)


passdaverificare = "ciao"
risultatoquery = "xxxxxxxxxxx"
result = hashlib.md5(passdaverificare.encode()).hexdigest()

print(risultatoquery == result)


#esempio inserimento

nome = "stefano"
password = "password"

passcript = hashlib.md5(password.encode()).hexdigest() #e si salva questa nel database
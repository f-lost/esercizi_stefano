# def decoratore(funzione):
#     def wrapper():
#         print("Prima dell'esecuzione della funzione")
#         funzione()
#         print("Dopo l'esecuzione della funzione")
#     return wrapper


# @decoratore
# def saluta():
#     print("Ciao!")



# saluta()

# def decoratore_con_argomenti(funzione):
#     def wrapper(*args, **kwargs):
#         print("Prima")
#         risultato = funzione(*args, **kwargs)
#         print("Dopo")
#         return risultato
#     return wrapper

# @decoratore_con_argomenti
# def somma(a,b):
#     return a+b

# print(somma(3,4))

# def logger(funzione):
#     def wrapper(*args,**kwargs):
#         print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
#         risultato = funzione(*args, **kwargs)
#         print(f"Risultato di {funzione.__name__}:{risultato}")
#         return risultato
#     return wrapper

# @logger
# def moltiplica(a,b):
#     return a*b



# moltiplica(3,4)


# def decoratore(funzione1,funzione2):
#     def wrapper(*args, **kwargs):
#         choice=True
#         while choice:
#             scelta = input("Area quadrato o Area Triangolo?")
#             if scelta == "q":
#                 risultato = funzione1(*args, **kwargs)
#             elif scelta == "t":
#                 risultato = funzione2(*args, **kwargs)
#             else:
#                 choice = False  


# def decoratore(funzione):
#     def wrapper(*args, **kwargs):
#         choice = True

#         while choice:
#             scelta = input("Vuoi calcolare l\' area o uscire?").lower()
#             if scelta == "area" or scelta == "a":
#                 risultato = funzione(*args, **kwargs)
#                 return risultato
#             else:
#                 choice = False
            
#     return wrapper        

            

# @decoratore
# def area_triangolo(b,h):
#     return (b*h)/2

# @decoratore
# def area_quadrato(l):
#     return l*l


# risultato = area_triangolo(2,3)
# print(risultato)


# def comprimi_stringa(stringa):
#     stringa_lista = list(stringa)
#     stringa_compressa = [stringa_lista[0]]
#     i = 0
#     while i < len(stringa_lista):
#         counter = 0
#         print("FLAG")
#         for j in range(len(stringa_lista)):
#             print("FLAG1")
#             if stringa_lista[j] == stringa_compressa[i]:
#                 counter += 1
#             stringa_compressa.append(counter)
#         i += counter-1
#     return stringa_compressa

# stringa_compressa = comprimi_stringa("aaabbc")
# print(stringa_compressa)





def decoratore(funzione):
    def wrapper():
        stringa=input("Digita una stringa: ")
        stringa_compressa = funzione(stringa)
        if len(stringa_compressa) <= len(stringa):
            print(stringa_compressa)
        else:
            print(stringa)
    return wrapper



@decoratore
def comprimi_stringa(stringa):

    stringa_compressa=[]
    lettera=stringa[0]
    counter = 1

    for i in range(1,len(stringa)):
        if stringa[i] == lettera:
            counter += 1
        else:
            stringa_compressa.append(f"{lettera}{counter}")
            lettera = stringa[i]
            counter = 1
    
    stringa_compressa.append(f"{lettera}{counter}")

    stringa_compressa = "".join(stringa_compressa)

    return stringa_compressa

comprimi_stringa()
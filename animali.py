class Animale:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        pass

class Leone(Animale):
    
    def fai_suono(self):
        print("Roar")


class Giraffa(Animale):

    def fai_suono(self):
        print("Boh")
    

class Pinguino(Animale):

    def fai_suono(self):
        print("Verso del pinguino")
        

class Tigre(Animale):

    def fai_suono(self):
        print("Roar (Tigre)")
        

class Zoo:

    zoo = []
    def __init__(self, nome):
        self.nome = nome
    def aggiungi_animale(self,animale):
        self.zoo.append(animale)

    def aggiungi_nuovi_animali(self,n):
    
        for i in range(n):
            choice = input(f"L'animale #{i+1} che animale è? (Leone/Giraffa/Pinguino/Tigre)").lower()
            
            if choice == "leone":
                nome = input("Qual è il suo nome?: ")
                eta = int(input("Qual è la sua età?: "))
                self.zoo.append(Leone(nome,eta))
                
            elif choice == "giraffa":
                nome = input("Qual è il suo nome?: ")
                eta = int(input("Qual è la sua età?: "))
                self.zoo.append(Giraffa(nome,eta))

            elif choice == "pinguino":
                nome = input("Qual è il suo nome?: ")
                eta = int(input("Qual è la sua età?: "))
                self.zoo.append(Pinguino(nome,eta))
            
            elif choice == "tigre":
                nome = input("Qual è il suo nome?: ")
                eta = int(input("Qual è la sua età?: "))
                self.zoo.append(Tigre(nome,eta))
            
            else:
                print("Animale non presente nella lista")

    def allarme_zoo(self):
        for i in range(len(self.zoo)):
            self.zoo[i].fai_suono()



leone1 = Leone("Alex",12)


prova_zoo=Zoo("Prova Zoo")

prova_zoo.aggiungi_nuovi_animali(3)

prova_zoo.allarme_zoo()

prova_zoo.aggiungi_animale(leone1)

prova_zoo.allarme_zoo()
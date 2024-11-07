from abc import ABC, abstractmethod

class Operaio:
    
    def __init__(self, nome, età):
        
        self.nome = nome
        self.età = età
    
    def lavora(self):

        print(f"{self.nome} sta lavorando...")


class Strumento(ABC):

    @abstractmethod
    def usa_strumento(self):
        pass


class Cazzuola(Strumento):
    
    def usa_strumento(self):
        
        print(f"sto spalmando la malta")


class Pennello(Strumento):
    
    def usa_strumento(self):
        
        print(f"sto pittando")
    

class Muratore(Operaio, Cazzuola):
    
    def __init__(self, nome, età):
        
        super().__init__(nome, età)
    

class Pittore(Operaio, Pennello):
    
    def __init__(self, nome, età):
        
        super().__init__(nome, età)



#test

pittore = Pittore ("Luigi", 25)
muratore = Muratore("Mario", 30)

pittore.usa_strumento()
muratore.usa_strumento()
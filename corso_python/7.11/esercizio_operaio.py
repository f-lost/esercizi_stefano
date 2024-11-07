from abc import ABC, abstractmethod

class Operaio:
    
    def __init__(self, nome, età):
        
        self.nome = nome
        self.età = età
    
    def lavora(self):

        print(f"{self.nome} sta lavorando...")


class Cazzuola(ABC):
    
    @abstractmethod
    def spalma_malta(self):
        pass


class Pennello(ABC):
    
    @abstractmethod
    def pitta(self):
        pass
    

class Muratore(Operaio, Cazzuola):
    
    def __init__(self, nome, età):
        
        super().__init__(nome, età)

    def spalma_malta(self):
        
        print(f"{self.nome} sta spalmando la malta")

    

class Pittore(Operaio, Pennello):
    
    def __init__(self, nome, età):
        
        super().__init__(nome, età)

    def pitta(self):

        print(f"{self.nome} sta pittando")
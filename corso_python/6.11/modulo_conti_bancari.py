class ContoBancario:

    def __init__(self):

        self.__titolare = ""
        self.__saldo = 0

    def deposita(self, importo):
        if self.__positivo(importo):
            self.__saldo += importo
            print(f"È stato effettuato un deposito di {importo}€ ")

    def preleva(self, importo):
        if  self.__positivo(importo) and self.__saldo > importo:
            self.__saldo -= importo
            print(f"È stato effettuato un prelievo di {importo}€ ")

    def visualizza_saldo(self):
        print(f"Il saldo attuale è {self.__saldo}€")

    def get_titolare(self):

        return self.__titolare

    def set_titolare(self, titolare):
        
        self.__titolare = titolare

    def set_saldo(self, saldo):

        self.__saldo = saldo

    def __positivo(self,importo):
        if importo >= 0:
            self.x = True #potevo fare una funzione privata getter che s
            return self.x
        else:
            print("Errore: importo negativo")



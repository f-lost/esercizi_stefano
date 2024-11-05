class ContoBancario:

    def __init__(self):

        self.__titolare = ""
        self.__saldo = 0

    def deposita(self, importo):
        if importo >= 0:
            self.__saldo += importo
            print(f"È stato effettuato un deposito di {importo}€ ")

    def preleva(self, importo):
        if  importo > 0 and self.__saldo > importo:
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



#test
conto1 = ContoBancario()

conto1.set_titolare("Stefano")

conto1.set_saldo(10)

conto1.visualizza_saldo()

conto1.deposita(5)

conto1.preleva(10)

conto1.visualizza_saldo()


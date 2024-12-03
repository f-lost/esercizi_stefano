class ContoBancario:
    """
    Classe che rappresenta un conto bancario con funzionalità base per depositi, prelievi e gestione del saldo.
    """

    def __init__(self):
        """
        Inizializza il conto con un titolare vuoto e un saldo iniziale di 0.
        """
        self.__titolare = ""
        self.__saldo = 0

    def deposita(self, importo):
        """
        Aggiunge un importo al saldo, se positivo.
        """
        if self.__positivo(importo):
            self.__saldo += importo
            print(f"È stato effettuato un deposito di {importo}€")

    def preleva(self, importo):
        """
        Sottrae un importo dal saldo, se positivo e se sufficiente.
        """
        if self.__positivo(importo) and self.__saldo >= importo:
            self.__saldo -= importo
            print(f"È stato effettuato un prelievo di {importo}€")

    def visualizza_saldo(self):
        """
        Mostra il saldo attuale del conto.
        """
        print(f"Il saldo attuale è {self.__saldo}€")

    def get_titolare(self):
        """
        Restituisce il nome del titolare del conto.
        """
        return self.__titolare

    def set_titolare(self, titolare):
        """
        Imposta il nome del titolare del conto.
        """
        self.__titolare = titolare

    def set_saldo(self, saldo):
        """
        Imposta il saldo del conto.
        """
        self.__saldo = saldo

    def __positivo(self, importo):
        """
        Metodo privato: verifica se un importo è positivo.
        """
        if importo >= 0:
            return True
        else:
            print("Errore: importo negativo")
            return False


# Test della classe
conto1 = ContoBancario()

# Imposta titolare e saldo
conto1.set_titolare("Stefano")
conto1.set_saldo(10)

# Visualizza saldo
conto1.visualizza_saldo()

# Effettua un deposito e un prelievo non valido
conto1.deposita(5)
conto1.preleva(-2)

# Visualizza il saldo aggiornato
conto1.visualizza_saldo()

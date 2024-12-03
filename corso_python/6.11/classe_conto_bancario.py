import modulo_conto_bancario as conto


class MetodoPagamento(conto.ContoBancario):
    """
    Classe base per rappresentare un metodo di pagamento generico.
    """

    def effettua_pagamento(self, mittente, importo, intestatario):
        """
        Esegue un pagamento trasferendo fondi dal conto del mittente
        a quello dell'intestatario.
        """
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento generico di {importo}€ da {mittente.get_titolare()} verso: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")


class CartaDiCredito(MetodoPagamento):
    """
    Rappresenta un metodo di pagamento tramite carta di credito.
    """

    def effettua_pagamento(self, mittente, importo, intestatario):
        """
        Esegue un pagamento tramite carta di credito.
        """
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento tramite carta di credito di {importo}€ da {mittente.get_titolare()} verso: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")


class PayPal(MetodoPagamento):
    """
    Rappresenta un metodo di pagamento tramite PayPal.
    """

    def effettua_pagamento(self, mittente, importo, intestatario):
        """
        Esegue un pagamento tramite PayPal.
        """
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento tramite PayPal di {importo}€ da {mittente.get_titolare()} per: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")


class BonificoBancario(MetodoPagamento):
    """
    Rappresenta un metodo di pagamento tramite bonifico bancario.
    """

    def effettua_pagamento(self, mittente, importo, intestatario):
        """
        Esegue un pagamento tramite bonifico bancario.
        """
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento tramite Bonifico Bancario di {importo}€ da {mittente.get_titolare()} verso il conto: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")


class GestorePagamenti:
    """
    Gestisce pagamenti utilizzando un metodo di pagamento specifico.
    """

    def effettua_pagamento(self, mittente, importo, intestatario, metodo):
        """
        Esegue un pagamento utilizzando il metodo specificato.
        """
        if isinstance(metodo, MetodoPagamento):
            metodo.effettua_pagamento(mittente, importo, intestatario)
        else:
            print("Tipo non supportato")


# Test del sistema
conto1 = conto.ContoBancario()
conto1.set_titolare("Stefano")
conto1.set_saldo(100)

conto2 = conto.ContoBancario()
conto2.set_titolare("Riccardo")
conto2.set_saldo(100)

# Creazione dei metodi di pagamento
metodo1 = MetodoPagamento()
metodo2 = CartaDiCredito()
metodo3 = PayPal()
metodo4 = BonificoBancario()

# Test con metodo generico
metodo1.effettua_pagamento(conto1, 50, conto2)
conto1.visualizza_saldo()

# Test con GestorePagamenti
gestore = GestorePagamenti()
gestore.effettua_pagamento(conto1, 50, conto2, metodo1)
gestore.effettua_pagamento(conto2, 50, conto1, metodo2)
conto2.visualizza_saldo()

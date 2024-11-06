import modulo_conti_bancari as conto


class MetodoPagamento(conto.ContoBancario):
    
    def effettua_pagamento(self, mittente, importo, intestatario):
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento generico di {importo}€ da {mittente.get_titolare()} verso: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")

class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self, mittente, importo, intestatario):
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento tramite carta di credito di {importo}€ da {mittente.get_titolare()} verso: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")

        


class PayPal(MetodoPagamento):

    def effettua_pagamento(self, mittente, importo, intestatario):
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento tramite PayPal di {importo}€ da {mittente.get_titolare()} per: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")

        


class BonificoBancario(MetodoPagamento):

    def effettua_pagamento(self, mittente, importo, intestatario):
        if isinstance(mittente, conto.ContoBancario) and isinstance(intestatario, conto.ContoBancario):
            mittente.preleva(importo)
            intestatario.deposita(importo)
            print(f"Pagamento tramite Bonifico Bancario di {importo}€ da {mittente.get_titolare()} verso il conto: {intestatario.get_titolare()}")
        else:
            print("Prova a reinserire mittente e intestatario, tipi non supportati")



class GestorePagamenti:
    
    def effettua_pagamento(self, mittente, importo, intestatario, a):
        
        if isinstance(a, MetodoPagamento):
            a.effettua_pagamento(mittente, importo, intestatario)
        else:
            print("Tipo non supportato")



#test
conto1 = conto.ContoBancario()
conto1.set_titolare("Stefano")
conto1.set_saldo(100)

conto2 = conto.ContoBancario()
conto2.set_titolare("Riccardo")
conto2.set_saldo(100)

metodo1 = MetodoPagamento()
metodo2 = PayPal()

metodo1.effettua_pagamento(conto1, 50, conto2)
conto1.visualizza_saldo()

gestore = GestorePagamenti()

gestore.effettua_pagamento(conto1, 50, conto2, metodo2)
conto2.visualizza_saldo()
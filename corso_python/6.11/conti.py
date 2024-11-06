class MetodoPagamento:
    
    def effettua_pagamento(self, importo):
        print(f"Pagamento generico di {importo}€")

class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento tramite carta di credito di {importo}€")


class PayPal(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento tramite PayPal di {importo}€")


class BonificoBancario(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print(f"Pagamento tramite Bonifico Bancario di {importo}€")


class GestorePagamenti:
    
    def effettua_pagamento(self, importo, a):
        
        if isinstance(a, MetodoPagamento):
            a.effettua_pagamento(importo)
        else:
            print("Tipo non supportato")



#test


metodo1 = MetodoPagamento()
print(isinstance(metodo1, MetodoPagamento))

metodo2 = PayPal()

metodo1.effettua_pagamento(50)

gestore = GestorePagamenti()

gestore.effettua_pagamento(50, metodo2)
class Teatro:
    
    def __init__(self):
        
        _posti = []
        pass

    def prenota_posto(self,numero,fila):
        pass

    def stampa_posti_occupati():
        pass


class Posto(Teatro):
    
    numero_corrente = 1    
    fila_corrente = "A"   
    posti_per_fila = 10  
    file_totali = 6

    def __init__(self):
        # Controlla se sono stati creati tutti i posti necessari
        if ord(Posto.fila_corrente) - ord('A') >= Posto.file_totali:
            print("Posti esauriti")
            return
        
        # Assegna il numero e la fila correnti
        self._numero = Posto.numero_corrente
        self._fila = Posto.fila_corrente
        
        # Incrementa il numero per il prossimo posto
        Posto.numero_corrente += 1
        
        # Se il numero supera i posti per fila, resetta il numero e passa alla fila successiva
        if Posto.numero_corrente > Posto.posti_per_fila:
            Posto.numero_corrente = 1
            Posto.fila_corrente = chr(ord(Posto.fila_corrente) + 1)

        self._occupato = 0


    def prenota(self):
        if self._occupato == 0:
            self.__set_occupato()
            print(f"Posto {self._fila}{self._numero} prenotato.")
        else:
            print("Posto già occupato.")

    def libera(self):
        if self._occupato == 1:
            self.__set_occupato()
            print(f"Posto {self._fila}{self._numero} liberato.")
        else:
            print("Posto già libero.")

    def get_numero(self):
        
        return self._numero

    def get_fila(self):
        
        return self._fila
       
    def __set_occupato(self):
        if self._occupato == 0:
            self._occupato = 1
        else:
            self._occupato = 0


class PostoVIP(Posto):
    
    accesso_lounge = 1

    def prenota():
        pass




class PostoStandard(Posto):
    
    pass




teatro1 = Teatro(10,6)
posto1 = Posto()
posto1.prenota()
class Menu:
    def __init__(self):
        self.__elementi = []  # Attributo privato per contenere gli elementi del menu
    
    def __get_elementi(self):
        return self.__elementi

    def __set_elementi(self, elementi):
        if isinstance(elementi, list):
            self.__elementi = elementi
        else:
            raise TypeError("Elementi deve essere una lista di oggetti Elemento")

    def aggiungi_elemento(self, elemento):
        """Aggiunge un elemento al menu."""
        if isinstance(elemento, Elemento):
            self.__elementi.append(elemento)
        else:
            raise TypeError("L'elemento deve essere un'istanza della classe Elemento")

    def rimuovi_elemento(self, nome):
        """Rimuove un elemento dal menu in base al nome."""
        self.__elementi = [el for el in self.__elementi if el.get_nome() != nome]
    
    def mostra_menu(self):
        """Mostra e gestisce il menu in un ciclo fino a quando l'utente sceglie di uscire."""
        while True:
            print("\nMenu:")
            for i, elemento in enumerate(self.__elementi, start=1):
                print(f"{i}. {elemento.get_nome()}")
            print(f"{len(self.__elementi) + 1}. Esci")

            try:
                scelta = int(input("Seleziona il numero dell'opzione: "))
                
                if 1 <= scelta <= len(self.__elementi):
                    # Esegue l'azione selezionata
                    self.__elementi[scelta - 1].esegui_azione()
                elif scelta == len(self.__elementi) + 1:
                    # Esce dal menu
                    print("Uscita dal menu.")
                    break
                else:
                    print("Scelta non valida. Riprova.")
            except ValueError:
                print("Per favore, inserisci un numero valido.")


class Elemento:
    def __init__(self, nome, azione=None):
        self.__nome = nome  # Attributo privato
        self.__azione = azione  # Attributo privato
    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Il nome deve essere una stringa")
    
    def esegui_azione(self):
        """Esegue l'azione associata a questo elemento."""
        if self.__azione:
            self.__azione.esegui()
        else:
            print(f"{self.__nome} non ha alcuna azione associata.")

    def get_azione(self):
        return self.__azione

    def set_azione(self, azione):
        if isinstance(azione, Azione):
            self.__azione = azione
        else:
            raise TypeError("Azione deve essere un'istanza della classe Azione")


class Azione:
    def __init__(self, funzione):
        self.__funzione = funzione  # Attributo privato
    
    def esegui(self):
        """Esegue la funzione associata all'azione."""
        if callable(self.__funzione):
            self.__funzione()
        else:
            raise ValueError("L'azione deve essere una funzione chiamabile")

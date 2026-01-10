
from threading import Lock

class Compte:

    verrou = Lock() 

    def __init__(self,solde, decouvert):
        self.solde = solde
        self.decouvert = decouvert


    def retrait(self, montant):
        with self.verrou:
            res = self.solde - montant
            if res >= self.decouvert:
                self.solde = res
                print("retrait de " + str(montant))
            else:
                print("retrait pas possible")


    def ajout(self, montant):
        with self.verrou:
            self.solde += montant
            print("ajout de " + str(montant))
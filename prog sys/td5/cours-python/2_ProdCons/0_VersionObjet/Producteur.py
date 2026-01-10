import threading
import time
import random

class Producteur(threading.Thread):
    def __init__(self, donnee, nom):
        super().__init__()
        self.donnee = donnee
        self.nom = nom

    def run(self):
        while True:
            item = random.randint(1, 100)  # Générer un élément aléatoire
            print(f"[{self.nom}] Produit {item}")
            self.donnee.produire(self.nom, item)
            time.sleep(random.uniform(0.5, 2))  # Simuler un délai
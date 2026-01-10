import threading
import time
import random

class Consommateur(threading.Thread):
    def __init__(self, donnee, nom):
        super().__init__()
        self.donnee = donnee
        self.nom = nom

    def run(self):
        while True:
            item = self.donnee.consommer(self.nom)
            time.sleep(random.uniform(0.5, 2))  # Simuler un délai
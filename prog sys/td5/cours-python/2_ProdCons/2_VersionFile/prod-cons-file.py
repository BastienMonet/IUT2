import random
from threading import Thread 
import queue
import time

# utilisation de la file d'attente thread-safe fournie par le module queue
# methode put et get qui permettent de gérer la synchronisation entre threads

class Producteur(Thread):
    def __init__(self, queue,nom):
        super().__init__()
        self.queue = queue
        self.nom = nom


    def run(self):
        while True:
            # Simuler la production d'un élément
            item = random.randint(1, 100)  # Générer un élément aléatoire
            self.queue.put(item)
            print(f"[{self.nom}] : Ajout de {item}, file ={self.queue.queue}")
            time.sleep(random.uniform(0.5, 2))  # Simuler un délai

class Consommateur(Thread):
    def __init__(self, queue,nom):
        super().__init__()
        self.queue = queue
        self.nom = nom

    def run(self):
        while True:
            # Consommer un élément de la file
            item = self.queue.get()
            print(f"[{self.nom}] : Consommation de {item}, file = {self.queue.queue}")
            time.sleep(random.uniform(0.5, 2))  # Simuler un délai

if __name__ == "__main__":
    # Créer une file d'attente
    q = queue.Queue(maxsize=2)

# Création des threads
threads = []

for i in range(2):  # 2 producteurs
    producteur = Producteur(q, nom=f"Producteur {i+1}")
    threads.append(producteur)
    producteur.start()

for i in range(3):  # 3 consommateurs
    consommateur = Consommateur(q, nom=f"Consommateur {i+1}")
    threads.append(consommateur)
    consommateur.start()

# Rejoindre les threads (optionnel dans ce cas car c'est un script infini)
for t in threads:
    t.join()

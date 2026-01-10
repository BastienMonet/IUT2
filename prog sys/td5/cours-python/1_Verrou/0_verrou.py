from threading import Thread, Lock
import time

class DonneePartagee:
    def __init__(self):
        self.compteur = 0
        self.lock = Lock()

    def incrementer(self):
        self.lock.acquire()  # Acquérir le verrou
        try:
            self.compteur += 1
        finally:
            self.lock.release()  # Libérer le verrou

    def decrementer(self):
        self.lock.acquire()  # Acquérir le verrou
        try:
            self.compteur -= 1
        finally:
            self.lock.release()  # Libérer le verrou

    def obtenir_valeur(self):
        self.lock.acquire()  # Acquérir le verrou
        try:
            return self.compteur
        finally:
            self.lock.release()  # Libérer le verrou

class IncrementerThread(Thread):
    def __init__(self, donnee):
        super().__init__()
        self.donnee = donnee

    def run(self):
        self.donnee.incrementer()

class DecrementerThread(Thread):
    def __init__(self, donnee):
        super().__init__()
        self.donnee = donnee

    def run(self):
        self.donnee.decrementer()

# Initialisation de la donnée partagée
donnee_partagee = DonneePartagee()

# Paramètres
iterations = 10

# Création des threads
thread_inc = IncrementerThread(donnee=donnee_partagee)
thread_dec = DecrementerThread(donnee=donnee_partagee)

# Démarrage des threads
thread_inc.start()
thread_dec.start()

# Attente de la fin des threads
thread_inc.join()
thread_dec.join()

# Afficher la valeur finale
valeur_finale = donnee_partagee.obtenir_valeur()
print(f"Valeur finale du compteur: {valeur_finale}")

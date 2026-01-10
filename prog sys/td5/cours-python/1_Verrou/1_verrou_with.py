import threading
import time

class DonneePartagee:
    def __init__(self):
        self.compteur = 0
        self.lock = threading.Lock()

    def incrementer(self, nom):
        with self.lock:  # Protéger l'accès à la donnée partagée
            self.compteur += 1
            print(f"[{nom}] Incrémente: Compteur = {self.compteur}")

    def decrementer(self, nom):
        with self.lock:  # Protéger l'accès à la donnée partagée
            self.compteur -= 1
            print(f"[{nom}] Décrémente: Compteur = {self.compteur}")

    def obtenir_valeur(self):
        with self.lock:  # Protéger la lecture
            return self.compteur

class IncrementerThread(threading.Thread):
    def __init__(self, donnee, nom, iterations):
        super().__init__()
        self.donnee = donnee
        self.nom = nom
        self.iterations = iterations

    def run(self):
        for _ in range(self.iterations):
            self.donnee.incrementer(self.nom)
            time.sleep(0.1)  # Simuler un délai

class DecrementerThread(threading.Thread):
    def __init__(self, donnee, nom, iterations):
        super().__init__()
        self.donnee = donnee
        self.nom = nom
        self.iterations = iterations

    def run(self):
        for _ in range(self.iterations):
            self.donnee.decrementer(self.nom)
            time.sleep(0.1)  # Simuler un délai

# Initialisation de la donnée partagée
donnee_partagee = DonneePartagee()

# Paramètres
iterations = 10

# Création des threads
thread_inc = IncrementerThread(donnee=donnee_partagee, nom="Thread-Incrémenter", iterations=iterations)
thread_dec = DecrementerThread(donnee=donnee_partagee, nom="Thread-Décrémenter", iterations=iterations)

# Démarrage des threads
thread_inc.start()
thread_dec.start()

# Attente de la fin des threads
thread_inc.join()
thread_dec.join()

# Afficher la valeur finale
valeur_finale = donnee_partagee.obtenir_valeur()
print(f"Valeur finale du compteur: {valeur_finale}")

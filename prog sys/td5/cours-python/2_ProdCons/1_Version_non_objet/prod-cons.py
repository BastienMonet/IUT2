import threading
import time
import random

# Buffer partagé et sa capacité
BUFFER_SIZE = 5
buffer = []

# Lock et conditions
lock = threading.Lock()
not_empty = threading.Condition(lock)
not_full = threading.Condition(lock)

def producteur():
    global buffer
    while True:
        item = random.randint(1, 100)  # Générer un élément aléatoire
        with not_full:  # Accès conditionnel au buffer
            while len(buffer) == BUFFER_SIZE:
                print("[Producteur] Buffer plein, en attente...")
                not_full.wait()  # Attendre qu'il y ait de la place
            buffer.append(item)  # Ajouter l'élément au buffer
            print(f"[Producteur] Produit: {item}. Buffer: {buffer}")
            not_empty.notify()  # Notifier qu'il y a un élément disponible
        time.sleep(random.uniform(0.5, 2))  # Simuler un délai

def consommateur():
    global buffer
    while True:
        with not_empty:  # Accès conditionnel au Buffer
            while len(buffer) == 0:
                print("[Consommateur] Buffer vide, en attente...")
                not_empty.wait()  # Attendre qu'il y ait un élément
            item = buffer.pop(0)  # Retirer l'élément du Buffer
            print(f"[Consommateur] Consommé: {item}. Buffer: {buffer}")
            not_full.notify()  # Notifier qu'il y a de la place disponible
        time.sleep(random.uniform(0.5, 2))  # Simuler un délai

# Création des threads producteur et consommateur
threads = []
for _ in range(2):  # 2 producteurs
    t = threading.Thread(target=producteur)
    threads.append(t)
    t.start()

for _ in range(3):  # 3 consommateurs
    t = threading.Thread(target=consommateur)
    threads.append(t)
    t.start()

# Rejoindre les threads (optionnel dans ce cas car c'est un script infini)
for t in threads:
    t.join()

import threading
import time
import random

class Donnee:
    def __init__(self, taille_max):
        self.buffer = []
        self.taille_max = taille_max
        self.lock = threading.Lock()
        # creation de deux conditions associées au verrou
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def produire(self, name, item):
        with self.lock:  # il est possible defaire un with sur la condition, le verrou associé sera acquis
            while len(self.buffer) == self.taille_max:
                print(f"[{name} ] Buffer plein, en attente...")
                self.not_full.wait()
            self.buffer.append(item) 
            print(f"[{name} ] Produit: {item}. Buffer: {self.buffer}")
            self.not_empty.notify()  #reveille un seul thread en attente sur not_empty (notify_all reveille tous les threads)

    def consommer(self,name):
        with self.lock:  
            while len(self.buffer) == 0:
                print(f"[{name}] Buffer vide, en attente...")
                self.not_empty.wait()
            item = self.buffer.pop(0) 
            print(f"[{name}] Consommé: {item}. Buffer: {self.buffer}")
            self.not_full.notify()  
        return item
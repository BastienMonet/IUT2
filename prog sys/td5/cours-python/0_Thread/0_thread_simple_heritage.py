from threading import Thread
import time

# heritage de la classe Thread
class T(Thread):
    
    def __init__(self, id):
        # appel du constructeur de la classe Thread
        super().__init__()
        self.id = id

    def run(self):
        print(f"Thread {self.id} en cours d'exécution")
        time.sleep(2)
        print(f"Thread {self.id} terminé")

t1 = T("1")
t2 = T("2")
t1.start()
t2.start()
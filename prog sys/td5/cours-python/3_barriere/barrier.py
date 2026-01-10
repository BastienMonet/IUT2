from threading import Thread
from threading import Barrier
import time

class MyThread(Thread):
    def __init__(self, barrier, data):
        super().__init__()
        self.barrier = barrier
        self.data = data

    def run(self):
        # Traitement spécifique à chaque thread avec les données
        while True:
            print(f"Thread {self.name} : Données = {self.data}")
            self.barrier.wait()
            print(f"Thread {self.name} a franchi la barrière.")
            time.sleep(1)

if __name__ == "__main__":
    nombre_threads = 5
    barrier = Barrier(nombre_threads)

    threads = []
    for i in range(nombre_threads):
        thread = MyThread(barrier, f"Données {i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
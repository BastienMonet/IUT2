from threading import Thread
import time

def code_thread(thread_id):
    print(f"Thread {thread_id} en cours d'exécution")
    time.sleep(2)
    print(f"Thread {thread_id} terminé")
    
# target indique la méthode à exécuter dans le thread. 
# L'argument 'args' doit être un tuple, donc on ajoute une virgule.

t1 = Thread(target=code_thread, args=(1,))
t2 = Thread(target=code_thread, args=(2,))
t1.start()
t2.start()
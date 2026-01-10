import concurrent.futures
import threading
from concurrent.futures import ThreadPoolExecutor

def task(x):
    # Tâche à exécuter par chaque thread
    print(f"Traitement de {x} par le thread {threading.get_ident()}")
    return x * x

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        # Soumission de tâches
        futures = [executor.submit(task, i) for i in range(10)]

        # Récupération des résultats
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(f"Resultat : {result}")

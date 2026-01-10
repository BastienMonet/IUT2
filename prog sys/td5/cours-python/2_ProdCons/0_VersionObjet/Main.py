from Producteur import Producteur
from Consommateur import Consommateur
from Donnee import Donnee

# Initialisation
TAILLE_TAMPON = 5
tampon = Donnee(TAILLE_TAMPON)

# Création des threads
threads = []

for i in range(2):  # 2 producteurs
    producteur = Producteur(tampon, nom=f"Producteur {i+1}")
    threads.append(producteur)
    producteur.start()

for i in range(3):  # 3 consommateurs
    consommateur = Consommateur(tampon, nom=f"Consommateur {i+1}")
    threads.append(consommateur)
    consommateur.start()

# Rejoindre les threads (optionnel dans ce cas car c'est un script infini)
for t in threads:
    t.join()
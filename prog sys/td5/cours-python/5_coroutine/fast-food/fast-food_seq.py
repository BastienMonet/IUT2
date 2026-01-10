from datetime import datetime
from time import sleep


def get_soda(client):
    print("    > Remplissage du soda pour {}".format(client))
    sleep(1)
    print("    < Le soda de {} est prêt".format(client))

def get_fries(client):
    print("    > Démarrage de la cuisson des frites pour {}".format(client))
    sleep(4)
    print("    < Les frites de {} sont prêtes".format(client))

def get_burger(client):
    print("    > Commande du burger en cuisine pour {}".format(client))
    sleep(3)
    print("    < Le burger de {} est prêt".format(client))

def serve(client):
    print("=> Commande passée par {}".format(client))
    start_time = datetime.now()
    get_soda(client)
    get_fries(client)
    get_burger(client)

    total = datetime.now() - start_time
    print("<= {} servi en {}".format(client, datetime.now() - start_time))
    return total


serve("toto")
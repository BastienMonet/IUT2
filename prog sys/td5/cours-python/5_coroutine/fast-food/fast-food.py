import asyncio
from datetime import datetime


async def get_soda(client):
    print("    > Remplissage du soda pour {}".format(client))
    await asyncio.sleep(1)
    print("    < Le soda de {} est prêt".format(client))

async def get_fries(client):
    print("    > Démarrage de la cuisson des frites pour {}".format(client))
    await asyncio.sleep(4)
    print("    < Les frites de {} sont prêtes".format(client))

async def get_burger(client):
    print("    > Commande du burger en cuisine pour {}".format(client))
    await asyncio.sleep(3)
    print("    < Le burger de {} est prêt".format(client))

async def serve(client):
    print("=> Commande passée par {}".format(client))
    start_time = datetime.now()
    task1 = asyncio.create_task(get_soda(client))
    task2 = asyncio.create_task(get_fries(client))
    task3 = asyncio.create_task(get_burger(client))
    await asyncio.gather(task1, task2, task3)
    total = datetime.now() - start_time
    print("<= {} servi en {}".format(client, datetime.now() - start_time))
    return total


asyncio.run(serve("toto"))
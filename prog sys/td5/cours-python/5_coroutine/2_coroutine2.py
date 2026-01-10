import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# Pour vraiment tirer parti des coroutines, il faut les exécuter de manière concurrente.
# La fonction asyncio.create_task() pour exécuter de manière concurrente des coroutines en tant que tâches asyncio.
# Les tâches servent à planifier des coroutines de façon à ce qu'elles s'exécutent de manière concurrente.
async def main():
    task1 = asyncio.create_task(
        say_after(5, 'hello'))

    task2 = asyncio.create_task(
        say_after(3, 'world'))

    print(f"started at {time.strftime('%X')}")

 
    # attente que les deux taches terminent, la durée doit etre la plus longue des deux
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

    # Le temps total d'exécution est d'environ 5 secondes, car les deux coroutines s'exécutent de manière concurrente.
    # 1. task1 commence, on rencontre await.asyncio.sleep(5) est appelé, la coroutine est mise en pause pendant 5 secondes.
    # 2. l'event loop peut maintenant exécuter d'autres tâches, donc task2 commence.
    # 3. task2 rencontre await.asyncio.sleep(3), elle est mise en pause pendant 3 secondes.
    # 4. l'envent loop est libre et attend que l'une des operations sleep se termine.
    # 5. après 3 secondes, l'event lopp reprend task2, et affiche "world"
    # 6. après 5 secondes, l'event loop reprend task1, et affiche "hello"


asyncio.run(main())
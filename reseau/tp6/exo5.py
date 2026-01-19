import asyncio

async def produire(queue ,name):
    while True:
        await asyncio.sleep(1)
        print(f'Produit: {name}')
        await queue.put(name)

async def consommer(queue):
    while True:
        name = await queue.get()
        await asyncio.sleep(2)
        print(f'Consommé: {name}')

async def main():
    queue = asyncio.Queue()

    # Lancer le consommateur
    consumer_task = asyncio.create_task(consommer(queue))

    # Produire des éléments
    await asyncio.gather(
        produire(queue, 'élément 1'),
        consommer(queue),
    )

asyncio.run(main())
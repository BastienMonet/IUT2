import asyncio

# ecriture d'application asynchrone avec la syntaxe async/await
# execution non concurrente

async def fetch_data():
    # Simuler une requête réseau qui prend 4 secondes
    await asyncio.sleep(10)
    print("data 1 recupérée")

async def fetch_data2():
    # Simuler une requête réseau qui prend 3 secondes
    await asyncio.sleep(3)
    print("data 2 recupérée")


async def fetch_data3():
    # Simuler une requête réseau qui prend 2 secondes
    await asyncio.sleep(2)
    print("data 3 recupérée")


async def main():
    # Appel des coroutines avec await
    await fetch_data()
    await fetch_data2()
    await fetch_data3()


asyncio.run(main()) 
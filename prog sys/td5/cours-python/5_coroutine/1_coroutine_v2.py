import asyncio

# ecriture d'application asynchrone avec la syntaxe async/await
# de maniere non concurrente

async def fetch_data():
    # Simuler une requête réseau qui prend 4 secondes
    await asyncio.sleep(10)
    return {"data": 42}

async def fetch_data2():
    # Simuler une requête réseau qui prend 3 secondes
    await asyncio.sleep(3)
    return {"data": 4}

async def fetch_data3():
    # Simuler une requête réseau qui prend 2 secondes
    await asyncio.sleep(2)
    print("toto")

async def main():
    # Appel des coroutines avec await
    result = await fetch_data()
    print("Après fetch_data")
    # apres avoir recuperer fech_data on passe a la suite
    result2 = await fetch_data2()
    print("Après fetch_data2")
    # apres avoir recuperer fech_data2 on passe a la suite
    await fetch_data3()
    # Affichage des résultats
    print(result)
    print(result2)

asyncio.run(main())
# importation du module pour la programmation asynchrone
import asyncio

# ecriture d'application asynchrone avec la syntaxe async/await

# definition de la coroutine avec le mot cle async def
async def fetch_data():
    # Simuler une requête réseau qui prend 2 secondes
    # utilisation d'une coroutine dans une coroutine (pas aillerus) avec le mot cle await
    # l'exectuion se suspend ici pour laisser la main a l'event loop
    await asyncio.sleep(2)
    return {"data": 42}

# definition d'une autre coroutine qui appelle la premiere, toujours avec await
async def main():
    result = await fetch_data()
    print(result)

# lancement de l'event loop et exécution de la coroutine principale
asyncio.run(main())
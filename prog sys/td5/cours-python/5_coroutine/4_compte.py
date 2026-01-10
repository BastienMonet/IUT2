import asyncio

async def compte_a_rebours(id, n):
    while n > 0:
        print(f"{id} : {n}")
        await asyncio.sleep(1)
        n -= 1

async def main():
    task = asyncio.create_task(compte_a_rebours(1,5))
    task2 = asyncio.create_task(compte_a_rebours(2,2))
    task3 = asyncio.create_task(compte_a_rebours(3,7))

    # lancement de trois comptes a rebours de maniere concurrente
    await task
    await task2
    await task3

asyncio.run(main())
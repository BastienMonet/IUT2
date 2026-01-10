import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

#Uitlisation de la fonction gather pour executer des coroutines de maniere concurrente
async def main():

    print(f"started at {time.strftime('%X')}")

    # utilisation de asyncio.gather pour executer des coroutines de maniere concurrente
    await asyncio.gather(
        say_after(5, 'hello'),
        say_after(3, 'world'),
    )
    print(f"finished at {time.strftime('%X')}")


    # version avec create_task et gather
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(
        say_after(5, 'hello'))

    task2 = asyncio.create_task(
        say_after(3, 'world'))
    await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
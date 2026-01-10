import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

#La classe asyncio.TaskGroup fournit une alternative plus moderne à create_task().
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(5, 'hello'))

        task2 = tg.create_task(
            say_after(3, 'world'))
        
        print(f"started at {time.strftime('%X')}")

    # le await est implicite
    
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
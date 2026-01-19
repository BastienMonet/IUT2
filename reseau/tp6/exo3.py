import asyncio
from time import perf_counter

async def download(name):
    print("debut du telechargement " + name)
    await asyncio.sleep(3)
    print("fin")

async def main():
    start = perf_counter()
    await asyncio.gather(
        download("1"),
        download("2"),
        download("3")
    )
    end = perf_counter()
    print(end - start)


asyncio.run(main())
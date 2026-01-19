import aiohttp
import asyncio


async def main():
    session = aiohttp.ClientSession()
    async with session as session:
        asyncio.gather(
            fetchdata('http://python.org', session),
            fetchdata('http://docs.python.org/3/', session),
        )


async def fetchdata(url, session):
    async with session.get(url) as response:
        return response.status


asyncio.run(main())
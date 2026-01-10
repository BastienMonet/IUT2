import asyncio
import aiohttp # a installer avec pip install aiohttp

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in ['https://www.python.org', 'https://www.google.com']:
            task = asyncio.create_task(fetch_page(session, url))
            tasks.append(task)

        # gather regroupe plusieurs et les excute de maniere concurrente. gather les lance toutes en meme temps et attends qu'elles soient terminées
        # $tasks est une liste de coroutines, on la "dépaquette" avec *tasks
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response[:50])

asyncio.run(main())
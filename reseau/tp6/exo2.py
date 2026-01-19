import asyncio

async def envoyer_email(nom):
    await asyncio.sleep(1)
    print(f"Email envoyé à {nom}")

async def main():
    await envoyer_email("Alice")
    await envoyer_email("Bob")
    await envoyer_email("Thomas")

asyncio.run(main())

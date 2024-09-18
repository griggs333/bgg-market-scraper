import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get("https://boardgamegeek.com/market/browse?objecttype=thing&objectid=67877&pageid=1&currency=USD&country=US") as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print(html)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
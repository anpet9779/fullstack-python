# mock fetch method

# https://httpbin.org/delay/10

import asyncio
import aiohttp


async def fetchUrl(session, url):
    async with session.get(url) as response:
        print(f"fetched {url} with status {response.status}") 


async def main():
    urls = [
        "https://httpbin.org/delay/10",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetchUrl(session, url) for url in urls]
        await asyncio.gather(*tasks) # '* ' unpacks the list works as spread operator

    print("All URLs fetched")

asyncio.run(main())
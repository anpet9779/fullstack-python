import asyncio
import time

from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}")
    time.sleep(1)
    return f"{item} is available"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            check_stock,
            "ginger"
        )

        print(result)

asyncio.run(main())


# Whole motive behind this code is to take heavy duty task and puth them all together in a separate thread instead of main thread
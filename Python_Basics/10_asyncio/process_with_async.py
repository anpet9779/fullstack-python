import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(message):
    return f"Encrypting {message[::-1]}"

async def main():
    if __name__ == "__main__":
        loop = asyncio.get_running_loop()
        with ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool,
                encrypt,
                "credit_Card_1234"
            )

            print(result)

asyncio.run(main())
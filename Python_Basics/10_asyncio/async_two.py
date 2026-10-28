import asyncio

async def brew(name):
    print(f"Brewing {name} chai")
    await asyncio.sleep(2) #here instead of asyncio.sleep(2) we can use time.sleep(2) which will result in executing every block simultaneously. Where asyncio.sleep(2) will result in one block
        
    print(f"{name} chai brewed")

async def main():
    await asyncio.gather(
        brew("ginger"), 
        brew("black")
    ) 
    #gather is like fork-join in JS

asyncio.run(main())


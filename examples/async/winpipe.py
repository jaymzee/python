import asyncio

async def tx1to2():
    com1 = await asyncio.open(r"\\.\pipe\lithium-COM1", "r")
    com2 = await asyncio.open(r"\\.\pipe\lithium-COM2", "w")
    while True:
        b = await com1.read(1)
        if len(b) == 0:
            break
        print("com1 got", b)
        asyncio.sleep(0.5)
        print("tx to com2", b)
        com2.write(b)

async def tx2to1():
    com1 = await asyncio.open(r"\\.\pipe\lithium-COM1", "w")
    com2 = await asyncio.open(r"\\.\pipe\lithium-COM2", "r")
    while True:
        b = await com2.read(1)
        if len(b) == 0:
            break
        print("com2 got", b)
        asyncio.sleep(0.5)
        print("tx to com1", b)
        com1.write(b)

async def main():
    asyncio.gather(tx1to2(), tx2to1())

asyncio.run(main())

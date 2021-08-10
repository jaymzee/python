import sys
import asyncio
import aiofiles


async def txrx(f1, f2, label):
    while True:
        b = await f1.read(1)
        if len(b) == 0:
            break
        print(label, "got", b)
        await asyncio.sleep(0.5)
        print(label, "sending", b)
        await f2.write(b)
        await f2.flush()


async def main(mode):
    com1 = await aiofiles.open(r"\\.\pipe\lithium-COM1", "r+")
    com2 = await aiofiles.open(r"\\.\pipe\lithium-COM2", "r+")
    if mode == 1:
        label = 'COM1 -> COM2'
        print(label)
        await txrx(com1, com2, label)
    elif mode == 2:
        label = 'COM2 -> COM1'
        print(label)
        await txrx(com2, com1, label)
    else:
        print('COM1 <-> COM2')
        await asyncio.gather(txrx(com1, com2, 'COM1 -> COM2'), txrx(com2, com1, 'COM1 <- COM2'))


if len(sys.argv) < 2:
    asyncio.run(main(0))
else:
    asyncio.run(main(int(sys.argv[1])))

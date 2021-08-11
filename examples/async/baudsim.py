import sys
import asyncio


async def txrx(reader, writer):
    while True:
        data = await reader.read(1)
        if len(data) == 0:
            break
        await asyncio.sleep(0.001)
        writer.write(data)
        await writer.drain()


async def main(mode):
    c1reader, c1writer = await asyncio.open_connection('127.0.0.1', 50001)
    c2reader, c2writer = await asyncio.open_connection('127.0.0.1', 50002)
    if mode == 1:
        print('COM1 -> COM2')
        await txrx(c1reader, c2writer)
    elif mode == 2:
        print('COM2 -> COM1')
        await txrx(c2reader, c1writer)
    else:
        print('COM1 <-> COM2')
        fwd = txrx(c1reader, c2writer)
        rev = txrx(c2reader, c1writer)
        await asyncio.gather(fwd, rev)


if len(sys.argv) < 2:
    asyncio.run(main(0))
else:
    asyncio.run(main(int(sys.argv[1])))

import sys
import asyncio


async def txrx(reader, writer, baud, localecho):
    while True:
        data = await reader.read(1)
        if len(data) == 0:
            break
        if localecho:
            sys.stdout.write(chr(data[0]))
            sys.stdout.flush()
        await asyncio.sleep(10 / baud)
        writer.write(data)
        await writer.drain()


async def main(baud):
    print('baud', baud)
    c1reader, c1writer = await asyncio.open_connection('127.0.0.1', 50001)
    c2reader, c2writer = await asyncio.open_connection('127.0.0.1', 50002)
    fwd = txrx(c1reader, c2writer, baud, True)
    rev = txrx(c2reader, c1writer, baud, False)
    await asyncio.gather(fwd, rev)


if len(sys.argv) < 2:
    asyncio.run(main(9600))
else:
    asyncio.run(main(float(sys.argv[1])))

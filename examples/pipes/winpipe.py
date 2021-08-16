import time
import sys


def echo(pipe):
    while True:
        rxb = pipe.read(1)
        if len(rxb) == 0 or rxb == b'~':
            break
        c = rxb[0]
        ch = chr(c) if c > 32 and c < 127 else ' '
        print('rx:', hex(c), ch)
        time.sleep(0.001)
        #print('tx:', hex(c), ch)
        pipe.write(rxb)


if len(sys.argv) > 1:
    filename = fr"\\.\pipe\{sys.argv[1]}"
    with open(filename, "wb+") as pipe:
        print(f'echoing {filename}')
        print('send a ~ to quit')
        echo(pipe)
else:
    print("Usage: winpipe pipename")
    exit(2)

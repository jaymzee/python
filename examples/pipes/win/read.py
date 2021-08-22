import time
import sys


def echo(pipe):
    while True:
        rxb = pipe.read(1)
        if len(rxb) == 0 or rxb == b'~':
            break
        c = rxb[0]
        ch = chr(c) if c >= 32 and c < 127 or c == 13 or c == 10 or c == 8 else '█'
        print(ch, end='')
        time.sleep(0.001)


if len(sys.argv) > 1:
    filename = fr"\\.\pipe\{sys.argv[1]}"
    with open(filename, "wb+") as pipe:
        print(f'reading {filename}')
        print('send a ~ to quit')
        echo(pipe)
else:
    print("Usage: winpiperd pipename")
    exit(2)

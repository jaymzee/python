import threading
import time
import sys
import os

running = True

def echo(pipe, file):
    while running:
        rxb = os.read(pipe, 1)
        if len(rxb) == 0 or rxb == b'~':
            break
        c = rxb[0]
        os.write(file,rxb)
        time.sleep(0.001)


def kb_task():
    input()
    print('key pressed - exiting')
    running = False
    os.close(file)
    os.close(pipe)
    kb_thread.kill()
    sys.exit(0)


if len(sys.argv) > 1:
    pipename = fr"\\.\pipe\{sys.argv[1]}"
    filename = sys.argv[2]
    pipe = os.open(pipename, os.O_RDWR)
    file = os.open(filename, os.O_CREAT | os.O_WRONLY)
    print(f'reading from pipe {pipename} and saving to file {filename}')
    print('press a key to quit')
    kb_thread = threading.Thread(target=kb_task, daemon=True).start()
    echo(pipe, file)
else:
    print("Usage: winpiperd pipename")
    exit(2)

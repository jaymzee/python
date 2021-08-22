"""
save data read from a windows pipe to a file
e.g. a serial port device in virtual box can use a windows pipe

a ~ indicates the end of transmission, so binary files should first
be base64 encoded then you add the ~ with echo ~ >>file
"""
import threading
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


def kb_task():
    input()
    print('key pressed - exiting')
    running = False
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
    os.close(file)
    os.close(pipe)
else:
    print("Usage: winpiperd pipename")
    exit(2)

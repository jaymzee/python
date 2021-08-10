import os
import time

com1 = open(r"\\.\pipe\lithium-COM1", "r")
com1fno = com1.fileno()

while True:
    #r, w, e = select([com1], [], [], 0)
    b = os.read(com1fno, 1)
    if len(b) == 0:
        break
    print(b)
    time.sleep(1)

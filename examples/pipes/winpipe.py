import time

com1 = open(r"\\.\pipe\lithium-COM1", "r")

while True:
    b = com1.read(1)
    if len(b) == 0:
        break
    print("got", b)
    time.sleep(1)

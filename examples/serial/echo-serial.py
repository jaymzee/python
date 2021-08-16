import serial
import sys
import time

def echo(sp):
    while True:
        if sp.inWaiting() > 0:
            data = sp.read()
            sp.write(data)
        else:
            data = ''
            time.sleep(0.1)
        print(sp.getDSR(), sp.getCTS(), sp.getCD(), sp.getRI(), data, '                        \r', end='')


if len(sys.argv) > 1:
    device = sys.argv[1]
    with serial.Serial(f'/dev/{device}') as ser:
        print(f"opened {ser.name}")
        echo(ser)
else:
    print("Usage: echo-serial device")

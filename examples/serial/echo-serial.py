import serial
import sys
import time

ctsstr = ['!CTS', ' CTS']
dsrstr = ['!DSR', ' DSR']
cdstr =  ['!CD', ' CD']
ristr =  ['!RI', ' RI']

def echo(sp):
    sp.setDTR(1)
    sp.setRTS(0)
    while True:
        rxrdy = sp.inWaiting()
        if rxrdy > 0:
            data = sp.read(rxrdy)
            sp.write(data)
        else:
            data = ''
            time.sleep(0.1)
        print(
            dsrstr[sp.getDSR()],
            ctsstr[sp.getCTS()],
            cdstr[sp.getCD()],
            ristr[sp.getRI()],
            '%4d' % len(data),
            data, ' ' * 30, '\r', end='')


if len(sys.argv) > 1:
    device = sys.argv[1]
    with serial.Serial(f'/dev/{device}', 1200) as ser:
        print(f"opened {ser.name}")
        echo(ser)
else:
    print("Usage: echo-serial device")



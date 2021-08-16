import serial
import sys
import time

ctsstr = ['!CTS', ' CTS']
dsrstr = ['!DSR', ' DSR']
cdstr =  ['!CD ', ' CD ']
ristr =  ['!RI ', ' RI ']

def echo(sp):
    while True:
        now = '\r' + time.asctime()
        sp.write(bytes(now, 'ascii'))
        time.sleep(1)
        count = sp.inWaiting()
        if count > 0:
            data = sp.read(count)
        else:
            data = ''
        print('\r',
            dsrstr[sp.getDSR()],
            ctsstr[sp.getCTS()],
            cdstr[sp.getCD()],
            ristr[sp.getRI()],
            data, ' ' * 30, end='')


if len(sys.argv) > 1:
    device = sys.argv[1]
    with serial.Serial(f'/dev/{device}') as ser:
        print(f"opened {ser.name}")
        echo(ser)
else:
    print("Usage: sender device")

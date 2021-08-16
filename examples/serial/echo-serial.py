import os
import serial
import sys
import time

ctsstr = ['\x1b[1;30m!CTS\x1b[m', ' CTS']
dsrstr = ['\x1b[1;30m!DSR\x1b[m', ' DSR']
cdstr =  ['\x1b[1;30m!CD\x1b[m', ' CD']
ristr =  ['\x1b[1;30m!RI\x1b[m', ' RI']

def echo(sp):
    sp.dtr = 1
    sp.rts = 1
    while True:
        rxrdy = sp.inWaiting()
        if rxrdy > 0:
            data = sp.read(rxrdy)
            sp.write(data)
        else:
            data = ''
            time.sleep(0.1)
        print(
            dsrstr[sp.dsr],
            ctsstr[sp.cts],
            cdstr[sp.cd],
            ristr[sp.ri],
            '%4d' % len(data),
            data, ' ' * 30, '\r', end='')


# enable color in Windows 10 Console
if os.environ.get('SESSIONNAME') == 'Console':
    os.system('color')

if len(sys.argv) > 1:
    device = sys.argv[1]
    with serial.Serial(device, 1200) as ser:
        print(f"opened {ser.name}")
        echo(ser)
else:
    print("Usage: echo-serial device")



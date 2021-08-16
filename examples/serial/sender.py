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
        now = '\r' + time.asctime()
        sp.write(bytes(now, 'ascii'))
        time.sleep(1)
        count = sp.inWaiting()
        if count > 0:
            data = sp.read(count)
        else:
            data = ''
        print('\r',
            dsrstr[sp.dsr],
            ctsstr[sp.cts],
            cdstr[sp.cd],
            ristr[sp.ri],
            data, ' ' * 30, end='')


if len(sys.argv) > 1:
    device = sys.argv[1]
    with serial.Serial(device, 1200) as ser:
        print(f"opened {ser.name}")
        echo(ser)
else:
    print("Usage: sender device")

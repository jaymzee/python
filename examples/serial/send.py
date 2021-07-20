import serial

ser = serial.Serial('/dev/ttyS5')
print(f"opened {ser.name}")
ser.write(b'hello, world!\n')
ser.close()

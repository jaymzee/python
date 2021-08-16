from serial.tools import list_ports

print('name\tdescription\tdevice\tmanufacturer\thwid')
for p in list_ports.comports():
    print(f'{p.name}\t{p.description!r}\t{p.device}\t{p.manufacturer!r}\t{p.hwid}')

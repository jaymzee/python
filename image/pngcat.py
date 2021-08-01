#!/usr/bin/env python3

import sys
from base64 import standard_b64encode


# a='T" -> transmit and display image
# f=100 -> PNG format
# f=24  -> 24-bit RGB
# f=32  -> 32-bit RGBA
def serialize_gfxcmd(**cmd):
    payload = cmd.pop('payload', None)
    head = ','.join('{}={}'.format(k, v) for k, v in cmd.items())
    resp = [b'\033_G', head.encode('ascii')]
    if payload:
        resp.extend([b';', payload])
    resp.append(b'\033\\')
    return b''.join(resp)


def write_chunked(**cmd):
    data = standard_b64encode(cmd.pop('data'))
    while data:
        chunk, data = data[:4096], data[4096:]
        m = 1 if data else 0
        sys.stdout.buffer.write(serialize_gfxcmd(payload=chunk, m=m, **cmd))
        sys.stdout.flush()
        cmd.clear()


if len(sys.argv) < 2:
    print("Usage: pngcat FILES")
    sys.exit(2)

for filename in sys.argv[1:]:
    with open(filename, 'rb') as f:
        data = f.read()
    write_chunked(a='T', f=100, data=data)
    sys.stdout.write(f'\n{filename}: {len(data)} bytes\n')

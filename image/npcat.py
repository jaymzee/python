#!/usr/bin/env python3

import sys
import itertools
from base64 import standard_b64encode

flatten = itertools.chain.from_iterable

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


def maximum(arr, init):
    m = init
    for r in arr:
        m = max(m, max(r))
    return m


def convert(filename):
    def to_rgb(v):
        v = int(255 * v / scale)
        return (v, v, v)

    with open(filename, 'r') as f:
        a = f.readlines()
    rows = [[int(v) for v in r.strip().split(' ')] for r in a if not r.startswith('#')]
    width, height = len(rows[0]), len(rows)
    scale = maximum(rows, 0)
    rgb = ((to_rgb(v) for v in r) for r in rows)
    data = bytes(flatten(flatten(rgb)))
    return width, height, data


if len(sys.argv) < 2:
    print("Usage: npcat FILES")
    sys.exit(2)

for filename in sys.argv[1:]:
    width, height, data = convert(filename)
    write_chunked(a='T', f=24, s=width, v=height, data=data)
    sys.stdout.write(f'\n{filename}: {width}x{height} {len(data)} bytes\n')

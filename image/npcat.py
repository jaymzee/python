#!/usr/bin/env python3

# display a numpy array (text format) in the kitty terminal

import sys
import itertools
from base64 import standard_b64encode

flatten = itertools.chain.from_iterable

# kitty stuff

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


# could use numpy to load the data but it's better to not have any dependencies
# and the file format is very simple

# return the maximum value in array
def maximum(arr, init):
    m = init
    for r in arr:
        m = max(m, max(r))
    return m


# return a list of lines from the txt file
def loadtxt(filenme):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


# parse the list of lines into a 2D array
def parsetxt(lines):
    arr = [[float(v) for v in ln.strip().split(' ')] for ln in lines if not ln.startswith('#')]
    width, height = len(arr[0]), len(arr)
    return width, height, arr


# convert the 2D array into rgb data bytes
def convert_to_rgb(width, height, rows):
    def to_rgb(v):
        v = int(255 * v / scale)
        return (v, v, v)
    scale = maximum(rows, 0)
    rgb = ((to_rgb(v) for v in r) for r in rows)
    data = bytes(flatten(flatten(rgb)))
    return width, height, data


if len(sys.argv) < 2:
    print("Usage: npcat FILES")
    sys.exit(2)

for filename in sys.argv[1:]:
    width, height, data = convert_to_rgb(*parsetxt(loadtxt(filename)))
    # a='T" -> transmit and display image
    # f=24  -> 24-bit RGB
    write_chunked(a='T', f=24, s=width, v=height, data=data)
    sys.stdout.write(f'\n{filename}: {width}x{height}\n')

#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print('Usage: wavplot file')
    sys.exit(2)

import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

def plot(filename, **kwargs):
    try:
        fs, x = wavfile.read(filename)
    except OSError as err:
        sys.stderr.write(f'{filename}: {err}\n')
        sys.exit(1)
    n = kwargs.get('n', f'{len(x)}').split(':')
    n = range(*(int(s) for s in n if s))
    plt.plot(n, x[n])
    channels = f'{x.shape[1]} channels' if x.ndim == 2 else '1 channel'
    plt.title(f'{filename}\n rate={fs} Hz; {len(n):,} samples; {channels}')
    plt.xlabel('n')
    plt.show()

if len(sys.argv) > 2:
    plot(sys.argv[1], n=sys.argv[-1])
else:
    plot(sys.argv[1])

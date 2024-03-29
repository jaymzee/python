import sys
import array
import fcntl
import termios
import struct
import time

def get_winsize():
    buf = array.array('H', [0, 0, 0, 0])
    fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, buf)
    return buf[0], buf[1]

_, COLS = get_winsize()

print(COLS)

def bold(msg):
    return u'\033[1m%s\033[0m' % msg

def progress(current, total):
    prefix = '%d / %d' % (current, total)
    bar_start = ' ['
    bar_end = '] '

    bar_size = COLS - len(prefix + bar_start + bar_end)
    amount = int(current / (total / float(bar_size)))
    remain = bar_size - amount

    bar = 'X' * amount + ' ' * remain
    return bold(prefix) + bar_start + bar + bar_end

NUM = 100
for i in range(NUM + 1):
    sys.stdout.write(progress(i, NUM) + '\r')
    sys.stdout.flush()
    time.sleep(0.05)
print('\n')

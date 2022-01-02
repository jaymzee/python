import os
import sys
import time


def bold(s):
    return f'\033[1m{s}\033[0m'


def highlight(s):
    return f'\033[1;32m{s}\033[0m'


def progress(current, total, cols):
    prefix = f'{current} / {total}'
    bar_start = " ["
    bar_end = "] "

    bar_size = cols - len(prefix+bar_start+bar_end)
    amount = int(current / total * bar_size)
    remain = bar_size - amount

    bar = "█" * amount + " " * remain

    if current < total:
        return bold(prefix) + bar_start + highlight(bar) + bar_end
    else:
        return "done." + " " * (cols - 5)


def main():
    NUM = 300
    cols = os.get_terminal_size()[0]
    for i in range(0, NUM, 10):
        bar = progress(i, NUM, cols)
        sys.stderr.write(bar + '\r')
        time.sleep(.1)
    bar = progress(NUM, NUM, cols)
    sys.stderr.write(bar + '\n')


if __name__ == '__main__':
    main()

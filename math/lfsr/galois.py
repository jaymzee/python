import sys

class lfsr(object):
    def __init__(self, poly, iv):
        self.poly = poly
        self.r = iv

    def shift(self):
        fb = self.r & 1
        self.r >>= 1
        if fb:
            self.r ^= self.poly

    def __repr__(self):
        return 'lfsr(%08x, %08x)' % (self.poly, self.r)

    def __taps(self):
        p = self.poly
        t = [0]
        c = 1
        while p:
            if p & 1:
                t.append(c)
            p = p >> 1
            c += 1
        c -= 1
        return c, t

    def taps1(self):
        c, t = self.__taps()
        t.sort(reverse=True)
        return t

    def taps2(self):
        c, t = self.__taps()
        return [c-x for x in t]

def gen_table():
    for i in range(32):
        pn = lfsr(i, 1)
        print("taps2 0x%02x: %s" % (i, pn.taps2()))

if __name__ == '__main__':
    period = 0
    poly = 0xaa2255dd
    iv = 1
    print_max = 16
    if len(sys.argv) > 1:
        poly = int(sys.argv[1], 16)
    if len(sys.argv) > 2:
        iv = int(sys.argv[2], 16)
    if len(sys.argv) > 3:
        print_max = int(sys.argv[3], 0)

    pn = lfsr(poly, iv)

    print('taps1: %s' % pn.taps1())
    print('taps2: %s' % pn.taps2())
    while True:
        if period < print_max:
            print("%s = %d" % (pn, pn.r & 1))
        pn.shift()
        period += 1
        if pn.r == iv:
            break

    print('period = %d' % period)

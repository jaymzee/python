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

    def taps1(self):
        p = self.poly
        t = [0]
        c = 1
        while p:
            if p & 1:
                t.append(c)
            p = p >> 1
            c += 1
        c -= 1
        t.sort(reverse=True)
        return t

    def taps2(self):
        p = self.poly
        t = [0]
        c = 1
        while p:
            if p & 1:
                t.append(c)
            p = p >> 1
            c += 1
        c -= 1
        t = [c-x for x in t]
        return t

def table():
    for i in range(32):
        pn = lfsr(i, 1)
        print(pn.taps(), "0x%02x" % i)

if __name__ == '__main__':
    #pn = lfsr(0xaa2255dd, 1)
    cfg = 0x402
    if len(sys.argv) > 1:
        cfg = int(sys.argv[1], 16)
    pn = lfsr(cfg, 1)
    print('taps1', pn.taps1())
    print('taps2', pn.taps2())

    for i in range(16):
        print(pn)
        pn.shift()

    #pn = lfsr(0x500, 1)
    pn = lfsr(cfg, 1)
    #check maximal length code
    last = pn.r
    c = 0
    while True:
        #print(pn.r)
        pn.shift()
        c += 1
        if pn.r == last:
            break
    print('count=%d' % c)

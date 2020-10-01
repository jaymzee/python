class lfsr(object):
    def __init__(self, poly, iv):
        self.poly = poly
        self.r = iv

    def shift(self):
        fb = self.r & 1
        self.r = self.r >> 1
        if fb:
            self.r = self.r ^ self.poly

    def __repr__(self):
        return 'lfsr(%08x, %08x)' % (self.poly, self.r)

    def taps(self):
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

if __name__ == '__main__':
    pn = lfsr(0xaa2255dd, 1)
    print(pn.taps())

    for i in range(16):
        print(pn)
        pn.shift()

    pn = lfsr(0x500, 1)
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



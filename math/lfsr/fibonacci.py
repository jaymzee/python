# polynomial x^16 + x^14 + x13 + x^11 + 1
#
#       1                            11    13 14    16
#      -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#   ->|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#  |   -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#  |                                  v     v  v     v
#   ----------------------------------+-----+--+-----+
#
#       1  2  3  4
#      -- -- -- --
#   ->|  |  |  |  |
#  |   -- -- -- --
#  |          v  v
#   -------------+

lfsr = 0x1
period = 0

while True:
    if period < 16:
        print(hex(lfsr), lfsr & 1)
    #bit = (lfsr >> 0) ^ (lfsr >> 2) ^ (lfsr >> 3) ^ (lfsr >> 5) & 1
    bit = (lfsr >> 0) ^ (lfsr >> 1) & 1
    lfsr = (lfsr >> 1) | (bit << 3) & 0xF
    period += 1
    if lfsr == 0x1:
        break

print(period)

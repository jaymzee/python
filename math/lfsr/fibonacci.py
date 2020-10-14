# polynomial x^16 + x^14 + x13 + x^11 + 1
#
#       1                            11    13 14    16
#      -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#   ->|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#  |   -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#  |                                  v     v  v     v
#   ----------------------------------+-----+--+-----+

lfsr = 0xACE1
period = 0

for i in range(16):
    print(hex(lfsr))
    bit = (lfsr >> 0) ^ (lfsr >> 2) ^ (lfsr >> 3) ^ (lfsr >> 5) & 1
    lfsr = (lfsr >> 1) | (bit << 15) & 0xFFFF
    period += 1
    if lfsr == 0xACE1:
        break

print(period)

K = 1024
M = 1024 * K
G = 1024 * M

ram = 948308 * K
vram = 76 * M
gpio = 16 * M

total = ram + vram + gpio
print(1 * G - total)


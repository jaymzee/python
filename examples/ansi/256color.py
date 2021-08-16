import os
import sys

# enable colors in Windows 10 Console
if os.environ.get('SESSIONNAME', '') == 'Console':
    os.system("color")

def print_color(val):
    sys.stdout.write(f'\033[48;5;{val}m ')

def print_colors(vals):
    for i, val in enumerate(vals):
        print_color(val)
        if i == 0:
            first = val
    sys.stdout.write(f'\033[m {first}..{val}\n')

print_colors(range(16))
for i in range(16, 232, 36):
    print_colors(i + j for j in range(36))
print_colors(range(232,  256))

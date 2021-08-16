import os

# enable colors in Windows 10 Console (better than colorama)
if os.environ.get('SESSIONNAME', '') == 'Console':
    os.system("color")

print('\033[1;31mHello\033[m')

import sys
import colorama

# Windows 10 CMD prompt does not have ANSI enabled by default
# this is easier than manually enabling the VIRTUAL_TERMINAL_PROCESSING flag
colorama.init()

sys.stdout.write('\033[1;31mHello\033[m\n')

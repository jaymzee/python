import re

s = 'The rain in Spain'
regex = '\w+ain'

print('search: ', re.search(regex, s))
print('findall: ', re.findall(regex, s))
print('finditer:')
for m in re.finditer(regex, s):
    print('  ', m.group(), m.span())

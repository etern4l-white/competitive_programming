import re

from string import ascii_letters, digits, printable
hi = input()
if len(hi) == 1:
    if hi[0] in ascii_letters and not hi[0] in '1234567890':
        print('Char')
    else:
        print('Integer')
else:


# print(len(re.findall(r"[a-zA-Z]+", "@#$%^&*")))
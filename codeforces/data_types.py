from string import ascii_letters, digits, printable

hi = input()
if len(hi) == 1:
    if hi[0] in printable and not hi[0] in '1234567890':
        print('Char')
    else:
        print('Integer')
else:
    iss = False
    iff = False
    for p, i in enumerate(hi):
        if i in printable and not i in '1234567890' and not i == '.':
            iss = True
            break
        elif i == '.' and p != 0 and p != len(hi)-1 and hi.count('.') == 1:
            iff = True
    if '.' in hi and not iff: iss = True
    if iss:
        print("String")
    else: 
        print("Float" if iff else "Integer")

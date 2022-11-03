alpha = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
for i in range(n):
    
    r = int(input())
    raw = input()
    p = [i for i in raw]
    if ' the ' in raw :
        for j, x in enumerate(p):
            p[j] = alpha[(alpha.index(p[j])+(26-r))%26] if p[j] != " " else ' '
    else:
        for j, x in enumerate(p):
            p[j] = alpha[(alpha.index(p[j])+r)%26] if p[j] != " " else ' '
    
    print(''.join(p))
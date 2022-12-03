n, l, r, x = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

def is_bit_on(i, j):
    return (i & (1<<j)) != 0

lenn = len(c)
ways = 0
for i in range(2**lenn):
    s = []
    for j in range(lenn):
        if is_bit_on(i, j):
            s.append(c[j])
    if s == []:continue
    minn = min(s)
    maxx = max(s)
    ss = sum(s)
    if maxx - minn >= x and ss >= l and ss <= r:
        ways+=1
print(ways)

    

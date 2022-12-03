def get_years(a,b):
    y = 0
    while a<=b :
        a*=3
        b*=2
        y+=1
    return y
d = {}
for i in range(1, 11):
    hi = {}
    for j in range(1,11):
        hi[j] = get_years(i, j)
    d[i] = hi

print(d[4][7])
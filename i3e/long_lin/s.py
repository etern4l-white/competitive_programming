n, h0, a, c, q = [int(i) for i in input().split()]

p = [h0]
for m in range(1, n):
    p.append((a*p[-1] + c)%q)

i = len(p)-1
r = 0

while i>=0:
    j = i-1
    last = p[i]
    o = p[i]
    while j>=0:
        if p[j] >=last:
            r+=1
            last = p[j]
        else:
            if p[j]<last and j!=i-1:
                break
            else:
                r+=1
        j-=1
    i-=1
print(r)
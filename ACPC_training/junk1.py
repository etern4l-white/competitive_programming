n = int(input())
for i in range(n):
    l, r = [int(i) for i in input().split()]
    s = l
    c = 1
    while s <= r:
        if s|c > r: break 
        else: s|=c
        c+=1
    print(s)

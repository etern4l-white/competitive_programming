input()
ns = sorted([int(i) for i in input().split()])
for i, n in enumerate(ns):
    if n != i+1:
        print(n-1)
        exit()
print(ns[-1]+1)
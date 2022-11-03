n, q = [int(i) for  i in input().split()]
di = {i+1:x for i,x in enumerate([int(i) for i in input().split()])}
all = ""
for i in range(q):
    p, d = [int(i) for i in input().split()]
    result = p
    if result == di[result]:
        all+=str(result) + "\n"
        continue
    while d > 0:
        result = di[result]
        d-=1
    all+=str(result) + "\n"
print(all, end="")

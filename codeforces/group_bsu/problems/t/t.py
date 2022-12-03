# n, bal = [int(i) for i in input().split()]
# print(bal - ((n//2)*(2 + n-1)))

n, bal = [int(i) for i in input().split()]
i = 1
while True:
    if bal >= i:
        bal-=i
    else:
        print(bal)
        break
    i+=1
    if i > n:
        i=1

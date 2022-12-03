import math
t = int(input())
for i in range(t):
    n = int(input())
    sum = int((n/2)*(2 + n - 1))
    l = int(math.log2(n))
    # print("----", l)
    for i in range(l+1):
        sum-=2*(2**i)
    # print("sum1", sum)
    sum2 = 0
    for i in range(1, n+1):
        if math.log2(i) == int(math.log2(i)):
            sum2-=i
        else:
            sum2+=i
    # print("sum2", sum2)
    if sum != sum2:
        print(n)
    print(sum, sum2)


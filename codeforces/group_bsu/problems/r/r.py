b, c, d = [int(i) for i in input().split()]
a = -1
for i in range(1, c+1):
    if (i+b)%c == d:
        a = i
        break
print(a)
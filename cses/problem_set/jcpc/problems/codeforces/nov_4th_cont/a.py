n = int(input())
for i in range(n):
    x, y, z = [int(i) for i in input().split()]
    if x>y:
        print(x)
    else:
        if z > (y-x):
            print(y)
        else:
            print(x+z + 2*(y-(x+z)))


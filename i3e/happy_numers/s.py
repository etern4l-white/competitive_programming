
def check_if_happy(n):
    while len(str(n)) > 1:
        n = sum([int(i)**2 for i in str(n)])
    return n==1
        
a, b = [int(i) for i in input().split()]
s = 0
for num in range(a, b+1):
    if check_if_happy(str(num)):
        print(num)
        s+=1
print(s)
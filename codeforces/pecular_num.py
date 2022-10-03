n = int(input())
ooo = n
fs = []
while n>1:
    for i in range(2, n+1):
        if n%i==0:
            fs.append(i)
            n//=i
            break
print(fs)
print("Yes" if sum(fs) == ooo-2 else "No")


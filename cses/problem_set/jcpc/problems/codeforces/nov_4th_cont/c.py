n = input()
arr = [i for i in input().split()]
even = []
odd = []
for i in arr:
    if len(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
p = 0
for i in even:
    for j in even:
        s = i+j
        l = len(s)
        fh = [int(i) for i in s[:l//2]]
        sh = [int(i) for i in s[l//2:]]
        if sum(fh) == sum(sh):
            p+=1


for i in odd:
    for j in odd:
        s = i+j
        l = len(s)
        fh = [int(i) for i in s[:l//2]]
        sh = [int(i) for i in s[l//2:]]
        if sum(fh) == sum(sh):
            p+=1
print(p)
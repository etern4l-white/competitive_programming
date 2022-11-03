n = int(input())
s = {}
for i in range(n):
    word = ''.join(sorted([i for i in input()]))
    if word not in s:
        s[word] = 1
    else:
        s[word]+=1
l = 0
for i in s:
    if s[i] > l:
        l=s[i]
print(l)
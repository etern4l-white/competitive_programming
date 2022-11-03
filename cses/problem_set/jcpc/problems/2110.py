s = input()
l = len(s)
sums = []
for i in range(1, l+1):
    arr = {}
    for j in range(0, l, i):
        arr[s[j:j+i]] = 1
    sums.append(len(list(arr.keys())))
print(' '.join([str(i) for i in sums]))
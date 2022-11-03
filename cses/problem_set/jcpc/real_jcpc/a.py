import itertools



# def get_xor(t):
#     b = len(bin(t)[2:]) - 1
#     hn = 2**b + 1
#     for i in range(b):
#         t^=hn
#         if t==0:break
#         hn>>=1
#         hn+=1

#     return t==0

# for t in range(255):
#     hi = get_xor(t)
#     if hi: print(t)

t = 63
b = len(bin(t)[2:]) - 1
s = []
hn = 2**b + 1
bins = bin(t)[2:]
print(bins)
ones = bins.count('1')
zeros = bins.count('0')
# print(ones, zeros)
if ones == 2 and bins[0] == '1' and bins[1] == '1':
    print(True)
elif ones%2==0 and zeros == 0:
    print(True)

s = 0
for i in range(b):
    s+=1
    t^=hn
    if t==0:break
    hn>>=1
    hn+=1
if t == 0:
    print(s)
else:
    print(-1)

# perms = itertools.permutations(s)
# print(t, list(perms))
def try_perms(t, perms):
    ss = []
    for perm in perms:
        s = 0
        tt = t
        for i in perm:
            tt^=i
            s+=1
            if tt == 0:ss.append(s)
    return -1 if len(ss) == 0 else min(ss)

# print(try_perms(t, perms))


"""
[1, 2, 3]
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 2, 1]
    [3, 1, 2]
]
"""
        
# def permute(lst):
#     if len(lst) == 1:
#         return lst
#     all = []
#     for i, x in enumerate(lst):
#         cur = [lst[i]]
#         new = lst[:i] + lst[i+1:]
#         cur.extend(permute(new))
#         all.append(cur)
#     return all

# print(permute(s))

# for i in s:
#     cur = [i]
#     for j in s:
#         if i == j:continue
#         cur.append(j)
#         # print(len(cur))
#         if len(cur) == 3:perm.append(cur)


# print((perm))


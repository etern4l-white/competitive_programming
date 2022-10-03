sen = input()
sub = input()
occs = sen.count(sub)
s = []

if occs > 0:
    for i in range(occs):
        if len(s) == 0:
            s.append(sen.index(sub)+1)
            continue
        s.append(sen.index(sub, s[-1]+1)+1)
    print(occs)
    print(' '.join([str(i) for i in s]))
else:
    print("Not found")

# print(sen.find())
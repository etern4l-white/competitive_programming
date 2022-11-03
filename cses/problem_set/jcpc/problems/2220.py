a, b = [int(i) for i in input().split()]
s = b-a
print(s)
z = 0
m1 = 0
m2 = 0
aa = a
bb = b

while(aa>0) :
    aa//=10
    m1+=1

while(bb>0) :
    bb//=10
    m2+=1

print(m1, m2)

for i in range(a, b+1):
    base = i//(10**(min(m1, m2)-1))
    for j in range(base):
        pass
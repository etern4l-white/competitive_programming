n = input()
s = []
cur = 0
m = 0
for i in n:
    
    if len(s) == 0:
        if i == "(":
            s.append(i)
        else:
            cur = 0
    else:
        if s[-1] == "(" and i == ")":
            s.pop(len(s)-1)
            cur+=2
        elif s[-1] == '(' and i == '(':
            s.append(i)
        elif i == '(':
            s.append(i)
        else:
            s = []
            cur = 0
        if cur >= m:
            m = cur
    # print(s)
print(m if m > 0 else -1)

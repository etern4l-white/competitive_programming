n = int(input())
rec = input().replace(" ", "")
nums = []
ops = []
for i in rec:
    if i == "+":
        ops.append(1)
    elif i == "-":
        ops.append(0)
    else:
        nums.append(int(i))
def is_bit_on(i, j):
    return (i & (1<<j)) != 0
s = nums[0]
org_sum = sum(nums)
nums = nums[1:]
found = False
minn = n-1
for i in range(2**(n-1)):
    arr = []
    ss = 0
    
    for j in range(n-1):
        if is_bit_on(i, j):
            arr.append(1)
            ss+=nums[j]
        else:
            arr.append(0)
            ss-=nums[j]
    if ss+s == 0:
        diff = 0
        for x in range(n-1):
            if arr[x] != ops[x]:
                diff+=1
        if diff <= minn:
            found = True
            minn = diff
if minn == n-1 and not found:
    print(-1 if org_sum!=0 else 0)
else:
    print(minn)
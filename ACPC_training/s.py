org = []
input()
arr = [int(i) for i in input().split()]
def gen_ss(index, sum, org):
    if index == len(arr) - 1:
        # print(sum)
        org.append(sum)
        return
    gen_ss(index+1, sum + arr[index], org)
    gen_ss(index+1, sum + arr[index+1], org)
gen_ss(0, 0, org)
# print(sorted(org))
org = sorted(org)
minn = 2**32
sss = sum(arr)
for i in range(len(org)-1):
    r = sss-org[i]
    if r < minn and r >=1:
        minn = r
    # print(r)
print(minn)
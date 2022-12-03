start, finish = [int(i) for i in input().split()]
summ = 0
org = []
lucky_index = 0
def gen(n, org, cur_step, finish, i):
    # print(n)
    if n != 0 and n >= i: 
        org.append(n)
        return
    if cur_step == 10 or n > finish:
        # print(cur_step)
        # print("hello", n)
        return
    gen(n*10 + 4, org, cur_step+1, finish, i)
    gen(n*10 + 7, org, cur_step+1, finish, i)

for i in range(start, finish+1):
    org = []
    l = len(str(i))
    gen(int('0' + '4'*(l-1)), org, l-1, finish, i)
    org = sorted(org)
    summ+=org[0]
    
print(summ)
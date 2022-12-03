start, finish = [int(i) for i in input().split()]
summ = 0
org = []
lucky_index = 0
def gen(n, org, cur_step):
    if n != 0: org.append(n)
    if cur_step == 10:
        return
    gen(n*10 + 4, org, cur_step+1)
    gen(n*10 + 7, org, cur_step+1)
gen(0, org, 0)
org = sorted(org)
print(len(org))
print(org)

for i in range(start, finish+1):
    while True:
        if org[lucky_index] >= i:
            summ+=org[lucky_index]
            break
        else:
            lucky_index+=1
print(summ)
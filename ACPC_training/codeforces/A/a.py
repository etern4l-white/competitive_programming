number = int(input())
sol = 0
org = []
def gen_lucky_number(n, s, f, curr_step, yes):
    if curr_step == 10:return
    if yes:
        if s == f:
            org.append(n)
    gen_lucky_number(n*10 + 4, s, f+1, curr_step+1, not yes)
    gen_lucky_number(n*10 + 7, s+1, f, curr_step+1, not yes)
gen_lucky_number(47, 1, 1, 1, True)
gen_lucky_number(44, 0, 2, 1, True)
gen_lucky_number(77, 2, 0, 1, True)
gen_lucky_number(74, 1, 1, 1, True)
org = sorted(org)
for i in org:
    if i >= number:
        print(i)
        break

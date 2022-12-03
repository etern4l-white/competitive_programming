def is_bit_on(x, i):
    return (x & (1<<i)) != 0
correct_sum = sum([1 if i == '+' else -1 for i in input()])
rec = input()
unknown = rec.count("?")
rest_sum = rec.count('+') - rec.count('-')
needed_sum = (correct_sum - rest_sum)
sums = 0
for i in range(2**unknown):
    curr_sum = 0
    for j in range(unknown):
        curr_sum +=1 if is_bit_on(i, j) else -1
    if curr_sum == needed_sum:
        sums+=1
if unknown == 0:
    print(f"%0.12f" % 1)
else:
    print(f"%0.12f" % (sums/(2**unknown)))
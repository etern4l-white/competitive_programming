n = int(input())
nums = [int(i) for i in input().split()]
m = 2**32
def is_bit_on(number, i):
	return (number & (1<<i)) != 0

for i in range(2**n):
	s = 0
	for j in range(n):
		if is_bit_on(i, j):
			s+=nums[j]
		else:
			s-=nums[j]
	s = abs(s)
	m=s if s < m else m
print(m)

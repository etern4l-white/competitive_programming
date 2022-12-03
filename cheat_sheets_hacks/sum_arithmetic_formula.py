"""
The formula for the sum of an arithmetic sequence is: S n = n 2 [ 2 a + ( n − 1 ) d ]
where: n = the number of terms to be added. a = the first term in the sequence.
"""

def get_sum_seq(start, diff, n):
    return int(((n/2)*(2*start + (n-1)*diff)))

hi = [i for i in range(1, 4)]
print(hi)
print(get_sum_seq(hi[0], 1, len(hi)))

""" Check if n is a power of m
"""
import math
def is_power_of_m(n, m):
    if n >=0:
        return n!= 0 and (m**(math.log(n,m)) == m**int(math.log(n,m)))
    else:
        n = -n
        return m**(math.log(n,m)) == m**int(math.log(n,m)) and int(math.log(n, m))%2==1

def gcdOfStrings(str1: str, str2: str) -> str:
    small = min(str1, str2)
    big = max(str1, str2)
    kernel_size = len(small)
    i = 0
    while kernel_size > 0:
        while i < len(big) - kernel_size+1:
            kernel = small[i:i+kernel_size]
            if big.replace(kernel, '') == '' and small.replace(kernel, '') == '': 
                return kernel
            i+=1
        kernel_size-=1
    return ''

str1 = "ABCABC"
str2 = "ABC"
correct = 'TAUXX'
out = "TAUXXTAUXXTAUXX"
res = gcdOfStrings(str1, str2)
hi = "asdfasdfasdfadsfkhaledfasdfasdf"
print(res)  
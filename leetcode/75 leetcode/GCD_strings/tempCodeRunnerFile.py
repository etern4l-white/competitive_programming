(str1, str2)
    kernel_size = len(small)
    i = 0
    while kernel_size > 0:
        while i < len(big) - kernel_size:
            kernel = small[i:i+kernel_size]
            if big.replace(kernel, '') == '': return kernel
            i+=1
        kernel_size-=1
    return ''
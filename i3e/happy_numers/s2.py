def see_if_happy(number):
    memory = [number]
    while True:
        number = sum([int(i)**2 for i in str(number)])
        
        if number == 1:
            return True
        if number in memory:
            return False
        memory.append(number)
    

a, b = [int(i) for i in input().split()]
happy = 0
for i in range(a, b+1):
    if see_if_happy(i):
        happy+=1
print(happy)
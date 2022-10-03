t = input()
n = sorted([int(i) for i in input().split()])
su = 0
for i in range(1, len(n)):
    
    su+=sum(n[i:])

print(su)

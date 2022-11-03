
for i in range(int(input())):
    d = {"G":0, "A":0,"B":0, "C":0,"D":0, "E":0, "F":0}
    s = input().upper()
    for j in s:
        if j in ['A', 'B', "C", "D", "E", "F", "G"]:
            d[j]+=1
    m = 0
    c = None
    for j in d:
        if d[j] > m:
            m = d[j]
            c = j
    print(c)











# # GKWsDJMfLKEiot

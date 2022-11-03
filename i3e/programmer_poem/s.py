UP = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

n, m = [int(i) for i in input().split()]
rhymes = [input() for i in range(n)]
input()
passage = [input().lower().split() for i in range(m)]
scheme_dict = {}
scheme = []
i = 0

for x, line in enumerate(passage):
    flagged = False
    for rhyme in rhymes:
        if line[-1] in rhyme.split():
            if x%2 == 1 and scheme[-1]=="X":
                flagged=False
                break
            flagged = True
            if rhyme not in scheme_dict:
                scheme_dict[rhyme] = UP[i]
                scheme.append(UP[i])
                i+=1
                break
            else:
                scheme.append(scheme_dict[rhyme])
                break
    if not flagged:
        scheme.append("X")
            
print(''.join(scheme))


# GKWsDJMfLKEiot
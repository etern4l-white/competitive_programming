n = int(input())
ts = [int(i) for i in input().split()]
hi = [[0]*n for i in range(n)]
for i, x in enumerate(ts):
    # if i == 0:continue
    hi[i][x-1] = 1
print('\n'.join([str(i) for i in hi]))
def dfs(i, j):
    sum = 0
    # row = i
    col = j
    while col < n:
        row = i
        while row < n:
            if hi[row][col] == 1:
                sum+=1
                sum+=dfs(0, row)
            row+=1
        # if row == n:
            # print(sum)
        col+=1
        # return sum
        if row == n and not col == n:
            # print(1)
            return sum
        elif col == n and row == n:
            # print(sum)
            print(sum)
            return sum
dfs(0,0)

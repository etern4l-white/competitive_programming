sample_input = """########
#..#...#
####.#.#
#..#...#
########"""

n, m = [int(i) for i in input().split()]
arr = []
for i in range(n):
    arr.append([i for i in input()])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

vis = [[0 for i in j] for j in arr]

def is_valid(i, j):
    return i >=0 and j>=0 and i<n and j<m and not vis[i][j] and arr[i][j] != '#'

s = 0


def dfs(i ,j):
    vis[i][j] = True
    cnt+=1
    if cnt == s-k:
        
    
    
    
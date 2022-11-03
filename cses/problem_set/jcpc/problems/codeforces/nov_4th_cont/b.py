
t = int(input())
for x in range(t):
    n = int(input())
    arr = sorted([ int(i) for i in input().split()])
    points = []
    for i in range(n):
        points.append([arr[n-i-1], arr[n+i]])
    sx = points[0][0]
    sy = points[0][1]
    for i in range(1, n):
        sx = abs(sx-points[i][0])
        sy = abs(sy-points[i][1])
    s = abs(sx) + abs(sy)
    print(s)
    for point in points:
        print(' '.join([str(point[0]), str(point[1])]))
        
    
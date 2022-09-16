import sys
input = lambda: sys.stdin.readline().strip()

def sol():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]
    for lst in c:
        for l in lst:
            print(l, end=' ')
        print()

sol()
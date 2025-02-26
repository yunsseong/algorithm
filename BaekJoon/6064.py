import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m, n, x, y = map(int, input().split())
    k = x
    flag = False
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            print(k)
            flag = True
            break
        else:
            k += m
    if not flag:
        print(-1)
import sys
import copy

def print_map(m):
    for i in range(r):
        print(''.join(m[i]))

r, c, n = list(map(int, input().split()))
m = []
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for _ in range(r):
    m.append(list(input()))

if n == 1:
    print_map(m)
    sys.exit()

if n % 2 == 0:
    for _ in range(r):
        print("O"*c)
    sys.exit()

cnt = 1

while cnt < n:
    bomb = []
    for i in range(r):
        for j in range(c):
            if m[i][j] == "O":
                bomb.append([i,j])
                m[i][j] = "."
            else:
                m[i][j] = "O"

    for i, j in bomb:
        for er, ec in zip(dr, dc):
            nr = i + er
            nc = j + ec

            if 0 <= nr < r and 0 <= nc < c:
                m[nr][nc] = "."
    cnt += 2
for i in range(r):
    print(''.join(m[i]))
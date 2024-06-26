h,w,x,y = list(map(int, input().split()))
b = []
for _ in range(h+x):
    b.append(list(map(int, input().split())))

for i in range(h-x):
    for j in range(w-y):
        b[x+i][y+j] = b[x+i][y+j] - b[i][j]

for i in range(h):
    for j in range(w):
        print(b[i][j], end = " ")
    print()
import sys

b = [int(input()) for _ in range(9)]
b.sort()
s = sum(b)
remain = s - 100
res = []
for i in range(9):
    for j in range(i, 9):
            if b[i] + b[j] == remain:
                for l in range(9):
                    if b[l] not in [b[i], b[j]]:
                        print(b[l])
                sys.exit()




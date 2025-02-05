n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(tree[k]) >= 2:
            print("yes")
        else:
            print("no")
        continue

    if t == 2:
        print("yes")

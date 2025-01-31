from collections import defaultdict

n = int(input())
l = [input().split() for _ in range(n)]
d = defaultdict(list)

for node, left, right in l:
    d[node] = [left, right]

def preorder(center):
    if center == ".":
        return

    print(center, end = "")
    preorder(d[center][0])
    preorder(d[center][1])

def inorder(center):
    if center == ".":
        return

    inorder(d[center][0])
    print(center, end = "")
    inorder(d[center][1])

def postorder(center):
    if center == ".":
        return

    postorder(d[center][0])
    postorder(d[center][1])
    print(center, end = "")

preorder("A")
print()
inorder("A")
print()
postorder("A")

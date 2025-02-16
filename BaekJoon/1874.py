from collections import deque
import sys

stack = []
answer = []
n = int(input())
targets = deque()
for _ in range(n):
    targets.append(int(input()))

cur = 1
prv = 0
while targets:
    target = targets.popleft()
    if cur <= target:
        while cur <= target:
            answer.append("+")
            stack.append(cur)
            cur += 1
        stack.pop()
        answer.append("-")

    if prv > target:
        tmp = stack.pop()
        if tmp == target:
            answer.append("-")
        else:
            print("NO")
            sys.exit()
    prv = target
print('\n'.join(answer))


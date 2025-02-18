import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = str(input())

p = "IOI"
cnt = 0
answer = 0

i = 0
while i < m - 1:
    if s[i:i+3] == p:
        cnt += 1
        i += 2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1
print(answer)
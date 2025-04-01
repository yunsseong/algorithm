import sys

ns = list(map(int, input().split()))
num = 1
while True:
    cnt = 0
    for i in ns:
        if num % i == 0:
            cnt += 1
    if cnt >= 3:
        print(num)
        sys.exit()
    else:
        cnt = 0
        num += 1
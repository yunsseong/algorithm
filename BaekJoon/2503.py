n = int(input())
e = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for case in list(map(str, range(111, 1000))):
    if "0" in case or len(set(list(case))) != len(case):
        continue
    for question, s, b in e:
        scnt = 0
        bcnt = 0
        for c, q in zip(list(case), list(str(question))):
            if c == q:
                scnt += 1
            else:
                if q in case:
                    bcnt += 1
        if scnt != s or bcnt != b:
            break
    else:
        cnt += 1
print(cnt)
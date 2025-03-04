from collections import deque
t = int(input())
for _ in range(t):
    cmd = list(input())
    n = int(input())
    d = deque()
    d.extend(input().strip("[").strip("]").split(","))

    direction = True

    flag = True

    for i in cmd:
        if i == "R":
            direction = not direction
        elif len(d) > 0 and d[0] != "":
            if direction:
                d.popleft()
            else:
                d.pop()
        else:
            flag = False

    if len(d) == 0 and len(cmd) == 1 and cmd[0] == "R":
        flag = True


    if flag:
        if not direction:
            d.reverse()
        print("[", ",".join(d), "]", sep="")
    else:
        print("error")


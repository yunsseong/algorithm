ls = sorted([int(input()) for _ in range(9)])
s, e = 0, 8
want = sum(ls) - 100
while s < e:
    if ls[s] + ls[e] == want:
        rm_s, rm_e = ls[s], ls[e]
        ls.remove(rm_s)
        ls.remove(rm_e)
        print(*ls, sep = "\n")
        break
    elif ls[s] + ls[e] < want:
        s += 1
    elif ls[s] + ls[e] > want:
        e -= 1



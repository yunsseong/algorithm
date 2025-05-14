n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))
ans = []
for i in ms:
    s, e = 0, n - 1
    res = 0
    while s <= e:
        mid = (s + e) // 2
        if cards[mid] == i:
           res = 1
           break
        elif cards[mid] < i:
            s = mid + 1
        else:
            e = mid - 1
    ans.append(res)
print(*ans)

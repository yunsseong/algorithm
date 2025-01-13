import copy

n = int(input())
card = list(map(int, input().split()))
card.insert(0, 0)
d = copy.copy(card)
d[1] = card[1]

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = min(d[i], d[i-j] + card[j])

print(d[n])

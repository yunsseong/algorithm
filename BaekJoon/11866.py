n, k = map(int, input().split())
num = [i for i in range(1, n + 1)]

idx = 0
answer = []
while num:
    idx = (idx + k - 1) % len(num)
    rem = num[idx]
    num.remove(num[idx])
    answer.append(rem)
print("<", ', '.join(map(str, answer)), ">", sep = "")


n, k = map(int, input().split())
num = [i for i in range(1, n + 1)]
idx = 0
answer = []
while num:
    idx = (idx + k - 1) % len(num)
    answer.append(str(num.pop(idx)))
print("<", ', '.join(answer), ">", sep = "")


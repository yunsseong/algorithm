n, a = map(int, input().split())
res = 0
b = a
while n // b != 0:
    res += n // b
    b *= a
print(res)
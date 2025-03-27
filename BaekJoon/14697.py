import sys

a, b, c, n = map(int, input().split())
if n % a == 0 or n % b == 0 or n % c == 0:
    print(1)
    sys.exit()

for i in range(n // a + 1):
    for j in range(n // b + 1):
        for k in range(n // c + 1):
            if a * i + b * j + c * k == n:
                print(1)
                sys.exit()
print(0)
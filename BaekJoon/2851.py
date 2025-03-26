psum = 0
p = 0
diff = 10000
res = 0
for i in range(10):
    p = int(input())
    psum += p
    if abs(100 - psum) <= diff:
        diff = abs(100 - psum)
        res = psum
print(res)
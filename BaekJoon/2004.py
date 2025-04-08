def num_count(n, a):
    cnt = 0
    b = a
    while n // b != 0:
        cnt += n // b
        b *= a
    return cnt

n, m = map(int, input().split())
cnt2, cnt5 = num_count(n, 2) - num_count(m, 2) - num_count(n - m, 2), num_count(n, 5) - num_count(m, 5) - num_count(n - m, 5)
print(min(cnt2, cnt5))
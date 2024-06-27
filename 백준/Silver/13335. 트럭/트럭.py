from collections import deque
n, w, l = list(map(int, input().split()))
t = deque(map(int, input().split()))
b = deque([0 for _ in range(w)])
bw = 0
cnt = 0

while t or bw != 0:
    if len(t) != 0:
        if bw - b[0] + t[0] <= l:
            truck_in = t.popleft()
            b.append(truck_in)
            bw += truck_in
        else:
            b.append(0)

    truck_out = b.popleft()
    bw -= truck_out
    cnt += 1
    
print(cnt)
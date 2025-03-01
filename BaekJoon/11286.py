import heapq
import sys
input = sys.stdin.readline
answer = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(answer, [abs(num), num])
    else:
        if len(answer) == 0:
            print(0)
        else:
            print(heapq.heappop(answer)[1])
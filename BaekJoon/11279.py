import heapq
import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
nums = []
for _ in range(n):
    i = int(input())
    if i > 0:
        heapq.heappush(nums, i * -1)
    else:
        if len(nums) == 0:
            print(0)
        else:
            print(heapq.heappop(nums) * -1)
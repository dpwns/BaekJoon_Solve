import sys
import heapq

input = sys.stdin.readline
n, l = map(int, input().split())
A = list(map(int, input().split()))

minh = list()
delh = list()
for i in range(n):
    heapq.heappush(minh, A[i])
    if i - l >= 0:
        heapq.heappush(delh, A[i - l])
    while delh != [] and minh[0] == delh[0]:
        heapq.heappop(minh)
        heapq.heappop(delh)
    print(minh[0], end=" ")

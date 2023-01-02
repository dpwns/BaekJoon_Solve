import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
s = []
ans = [-1 for _ in range(n)]
for i in range(n):
    if not s:
        s.append([l[i], i])
        continue
    while s and s[-1][0] < l[i]:
        temp = s.pop()
        ans[temp[1]] = l[i]
    s.append([l[i], i])
for i in ans:
    print(i, end=" ")

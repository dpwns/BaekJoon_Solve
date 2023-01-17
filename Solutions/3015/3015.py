import sys

input = sys.stdin.readline

n = int(input())
s = list()
cnt = 0
for _ in range(n):
    a = int(input())
    if not s:
        s.append([a, 1])
        continue
    while s and s[-1][0] < a:
        cnt += s[-1][1]
        s.pop()
    b = len(s)
    for i in range(1, b + 1):
        if s[b - i][0] == a:
            cnt += s[b - i][1]
        else:
            cnt += 1
            break
    if s and s[-1][0] == a:
        s[-1][1] += 1
    else:
        s.append([a, 1])
print(cnt)

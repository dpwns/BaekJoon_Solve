import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    for i in range(n + 1):
        s += i * (i + 1) * (i + 2) // 2
    print(s)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
x = [(a[i], p[i]) for i in range(n)]
x.sort()

m = [0 for _ in range(n)]
temp = sum(p)
s = []
for i in x:
    s.append(temp)
    temp -= i[1]

M = 0


def find(I, P, K, A):
    global M
    M = max(M, P)
    if I >= n or P + s[I] <= M:
        return
    if x[I][0] + A <= K:
        find(I + 1, P + x[I][1], K - x[I][0] - A, A + x[I][0])
        find(I + 1, P, K, A)


find(0, 0, k, 0)
print(M)

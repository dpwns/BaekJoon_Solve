l = [0 for _ in range(10)]
start = [False for _ in range(10)]
n = int(input())
for _ in range(n):
    a = input()
    g = len(a)
    start[ord(a[0]) - ord("A")] = True
    for i in range(g):
        l[ord(a[i]) - ord("A")] += 10 ** (g - i - 1)
mI = -1
for i in range(10):
    if start[i]:
        continue
    if mI == -1:
        mI = i
    elif l[i] < l[mI]:
        mI = i
l[mI] = 0
l.sort()
s = 0
for i in range(10):
    s += l[i] * i
print(s)

import sys
import math

input = sys.stdin.readline
t = int(input())
l = ["" for _ in range(1000001)]
l[2] = "()"
l[3] = "(())"
maxTemp = "(" * 50 + ")" * 50


def p(N):

    global maxTemp
    if l[N] != "":
        return l[N]
    minL = maxTemp
    temp1 = math.ceil(math.sqrt(N))
    for j in range(2, temp1 + 1):
        x, y = divmod(N, j)
        a, b = p(j), p(x)
        if a < b:
            temp = "(" * y + a + b + ")" * y
        else:
            temp = "(" * y + b + a + ")" * y
        if len(temp) < len(minL):
            minL = temp
        elif len(temp) == len(minL):
            minL = min(temp, minL)
    l[N] = minL
    return l[N]


for _ in range(t):
    print(p(int(input())))

import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    visit = [False for _ in range(20001)]
    q1 = [[1, "1"]]
    q2 = []
    n = int(input())
    flag = True
    cnt = 0
    if 1 % n == 0:
        print(1)
        flag = False
    visit[1] = True
    while flag and cnt < 100:
        for i in q1:
            a = (i[0] * 10) % n
            if a == 0:
                print(i[1] + "0")
                flag = False
                break
            elif not visit[a]:
                q2.append([a, i[1] + "0"])
                visit[a] = True
            b = (i[0] * 10 + 1) % n
            if b == 0:
                print(i[1] + "1")
                flag = False
                break
            elif not visit[b]:
                q2.append([b, i[1] + "1"])
                visit[b] = True
        cnt += 1
        q1 = q2
        q2 = []
    if flag:
        print("BRAK")

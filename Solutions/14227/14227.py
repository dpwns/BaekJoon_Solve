import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())

if a > c or b > d:
    print(-1)
    exit()

cnt = 0
while True:
    if c == a and d == b:
        break
    # 홀짝 다른경우
    if c & 1 != d & 1:
        temp1 = c - a
        temp2 = d - b
        if temp1 != temp2:
            print(-1)
            exit()
        else:
            cnt += temp1
            break
    # 둘다 홀수인경우
    elif c & 1 == 1:
        cnt += 1
        c -= 1
        d -= 1
    # 둘다 짝수인경우
    else:
        temp1 = c - a
        temp2 = d - b
        temp3 = c // 2
        temp4 = d // 2
        # 나눌 수 있는지 판정
        if temp3 >= a and temp4 >= b and abs(a - b) <= abs(temp3 - temp4):
            c = temp3
            d = temp4
            cnt += 1
        else:
            if temp1 == temp2:
                cnt += temp1
                break
            else:
                print(-1)
                exit()
    if a > c or b > d:
        print(-1)
        exit()

print(cnt)

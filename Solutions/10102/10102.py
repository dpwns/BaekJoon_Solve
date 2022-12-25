import sys

input = sys.stdin.readline
n = int(input())
a, b = 0, 0
inputString = input().strip()
for i in inputString:
    if i == "A":
        a += 1
    else:
        b += 1
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")

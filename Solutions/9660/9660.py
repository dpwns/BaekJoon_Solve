import sys

input = sys.stdin.readline
n = int(input())
n = n % 7
SK = [1, 3, 4, 5, 6]
if n in SK:
    print("SK")
else:
    print("CY")

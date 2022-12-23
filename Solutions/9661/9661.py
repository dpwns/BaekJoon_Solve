import sys

input = sys.stdin.readline
n = int(input())
l = ["CY", "SK", "CY", "SK", "SK"]
print(l[n % 5])

# 23 = 16 + 4 + 2 + 1
# 이진수로 표현한 것과 같음
import sys
input = sys.stdin.readline

n = int(input())

n = str(format(n, "b"))
print(n.count("1"))

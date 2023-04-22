# 구간의 합 = (첫번째 항 + 마지막 항) × 항의 개수 ÷ 2

a, b = map(int, input().split())
n = abs(a - b) + 1
sum = int(n * (a + b) / 2)
print(sum)

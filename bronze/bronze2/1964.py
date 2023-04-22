n = int(input())
first = 5
second = 7
for i in range(1, n):
    first += second
    second += 3
print(first % 45678)

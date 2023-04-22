num = int(input())
value = []

for i in range(0, num):
    a, b = map(int, input().split())
    value.append(str(a**b))

for j in range(0, num):
    print(value[j][-1])

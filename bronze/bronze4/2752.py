arr = []

value = list(map(int, input().split()))
value.sort()
for i in range(3):
    print(value[i], end=" ")

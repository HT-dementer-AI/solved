n = int(input())
array = []
for i in range(n):
    a, b = map(int, input().split())
    array.append(a + b)

for i in range(n):
    print(array[i])

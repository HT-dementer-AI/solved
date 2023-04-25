n = int(input())

array = []

for i in range(n):
    value = input()
    array.append(value)
    print(array[i][0] + array[i][-1])

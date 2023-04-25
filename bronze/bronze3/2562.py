array = []

for i in range(9):
    value = int(input())
    array.append(value)

print(max(array))
print(array.index(max(array)) + 1)

arry = []

for i in range(10):
    value = int(input())
    arry.append(value % 42)
arry = set(arry)
print(len(arry))

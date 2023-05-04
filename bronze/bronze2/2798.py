from itertools import combinations

result = []
a, b = map(int, input().split())
li = list(input().split())

for i in range(len(li) + 1):
    result = result + list(combinations(li, i))

for i in range(len(li) + 1):
    result[i] = list(result[i])
print(list(result[10]))

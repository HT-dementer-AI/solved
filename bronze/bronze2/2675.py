n = int(input())


for i in range(n):
    a, b = map(str, input().split())
    result = ""
    for j in range(len(b)):
        result = result + b[j] * int(a)
    print(result)

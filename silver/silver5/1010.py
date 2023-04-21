def combination(n, r):
    sum1 = 1
    sum2 = 1

    for i in range(r + 1, n + 1):
        sum1 *= i
    
    for i in range(1, n - r + 1):
        sum2 *= i

    result = sum1 / sum2

    return result

# 값 입력
testNum = int(input())
li = []

for i in range(0, testNum):
    r ,n = input().split()
    r = int(r)
    n = int(n)
    result = int(combination(n,r))
    li.append(result)

for i in range(0, testNum):
    print(li[i])

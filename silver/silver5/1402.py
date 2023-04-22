divisorList = []


def divisor(value):
    for i in range(1, value + 1):
        if (value % i == 0):
            divisorList.append(i)


def isRight(divisorList, b):
    reverseList = divisorList[::-1]
    for i in range(0, len(divisorList)):
        if (divisorList[i] + reverseList[i] == b):
            return divisorList[i] + reverseList[i]


num = int(input())

for i in range(0, num):
    a, b = map(int, input().split())
    divisor(a)

result = isRight(divisorList, b)
if (result == b):
    print("yes")
else:
    print("no")

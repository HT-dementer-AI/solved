import sys
input = sys.stdin.readline

l = int(input())
r = int(input())
n = int(input())
a, d = 1, 1
array = []

# 초기화
arithmetic_progression = 1

while (True):
    arithmetic_progression = n*(2*a + (n-1)*d)/2

    if (arithmetic_progression > r):
        preA = a
        preD = d
        a = a + 1
        d = 1
        if(preA < a and preD == 1):
            break

    else:
        if (l <= arithmetic_progression <= r):
            array.append(arithmetic_progression)
        d = d + 1

    print(a, d, arithmetic_progression)

print(len(set(array)))

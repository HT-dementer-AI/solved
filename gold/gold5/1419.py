# # <a 기준 출력>
# import sys
# input = sys.stdin.readline

# l = int(input())
# r = int(input())
# n = int(input())
# a, d = 1, 1
# array = []

# # 초기화
# arithmetic_progression = 1

# while (True):
#     arithmetic_progression = n*(2*a + (n-1)*d)/2
#     print(a, d, arithmetic_progression)

#     if (arithmetic_progression > r):
#         preA = a
#         preD = d
#         a = a + 1
#         d = 1
#         if(preA < a and preD == 1):
#             break

#     else:
#         if (l <= arithmetic_progression <= r):
#             array.append(arithmetic_progression)
#         d = d + 1


# print(len(set(array)))


# <d기준 출력>
import sys
input = sys.stdin.readline

l = int(input())
r = int(input())
n = int(input())
a, d = 1, 1
array = []
count = 0

# 초기화
arithmetic_progression = 1

while (True):
    arithmetic_progression = n*(2*a + (n-1)*d)/2
    print(a, d, arithmetic_progression)
    count += 1

    if (arithmetic_progression > r):
        preA = a
        preD = d
        d = d + 1
        a = 1
        if(preD < d and preA == 1):
            break

    else:
        if (l <= arithmetic_progression <= r):
            array.append(arithmetic_progression)
        a = a + 1


print(len(set(array)))

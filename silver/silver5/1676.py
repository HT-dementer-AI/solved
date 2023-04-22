# 코드 최적화 한거
num = int(input())
count = 0
fac = 1

while (num > 1):
    fac *= num
    num -= 1

for x in reversed(str(fac)):
    if (x != "0"):
        break
    count += 1

print(count)

# <이전코드>
# num = int(input())
# count = 0
# fac = 1

# while (True):
#     fac = fac * num
#     num = num - 1
#     if (num == 1):
#         fac = str(fac)
#         break

# for x in fac[::-1]:
#     if (x != "0"):
#         break
#     count += 1

# print(count)

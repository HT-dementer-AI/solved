first = input()

if(int(first) < 10):
    next = "0" + first
    first = "0" + first
else:
    next = first

dsum = ""
count = 0

# 각자리 더해주는 함수


def digitSum(n):
    if(int(n) < 10):
        return "0" + str(int(n))
    else:
        if(int(n[0]) + int(n[1]) < 10):
            return "0" + str(int(n[1]) + int(n[0]))
        else:
            return str(int(n[0]) + int(n[1]))


while(True):
    dsum = digitSum(next)
    # print(next, dsum)
    next = next[1] + dsum[1]
    count += 1
    if(str(next) == str(first)):
        break

print(count)

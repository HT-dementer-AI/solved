num = input()
global count
count = 0


def convert(num):
    global count
    sum = 0

    if(len(num) == 1):
        return num

    else:
        for i in range(0, len(num)):
            sum = sum + int(num[i])
        count = count + 1
        return convert(str(sum))


value = convert(num)
print(count)
if(int(value) % 3 == 0):
    print("YES")
else:
    print("NO")

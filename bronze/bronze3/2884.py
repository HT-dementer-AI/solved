a, b = map(int, input().split())


if(a == 0 and b < 45):
    a = 23
    b = b + 15
elif(b >= 45):
    b = b - 45
else:
    a = a - 1
    b = b + 15


print(a, b)

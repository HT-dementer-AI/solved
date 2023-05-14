while(True):

    x = list(map(int, input().split()))

    if(x[0] == 0 and x[1] == 0 and x[2] == 0):
        break
    x = sorted(x)
    if(x[2] ** 2 == x[0]**2 + x[1]**2):
        print("right")
    else:
        print("wrong")

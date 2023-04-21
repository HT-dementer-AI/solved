result = []

array = list(map(int, input().split()))

# 각각의 길이 구하는 함수


def coordistence(arr):
    aX = pow(arr[0] - arr[2], 2)
    bX = pow(arr[0] - arr[4], 2)
    cX = pow(arr[2] - arr[4], 2)

    aY = pow(arr[1] - arr[3], 2)
    bY = pow(arr[1] - arr[5], 2)
    cY = pow(arr[3] - arr[5], 2)

    aLen = pow(aX + aY, 1/2)
    bLen = pow(bX + bY, 1/2)
    cLen = pow(cX + cY, 1/2)

    return aLen, bLen, cLen


def isinclination(array):
    # if(array[0] == array[2] == array[4] or array[1] == array[3] == array[5]):
    #     return False
    # else:
    #     if(array[0] == 0 and array[2] == 0 and array[4] == 0 or array[1] == 0 and array[3] == 0 and array[5] == 0):
    #         return False
    #     else:
    #         aClin = (array[0] - array[2]) / (array[1] - array[3])
    #         bClin = (array[0] - array[4]) / (array[1] - array[5])
    #         cClin = (array[2] - array[4]) / (array[3] - array[5])
    #         if(aClin == bClin or aClin == cClin or bClin == cClin):
    #             return False
    if (array[2] - array[0]) * (array[5] - array[3]) == (array[4] - array[2]) * (array[3] - array[1]):
        return False


if(isinclination(array) == False):
    print("-1.0")
else:
    result = coordistence(array)
    max = max(result)*2
    min = min(result)*2
    difference = max - min
    print(difference)

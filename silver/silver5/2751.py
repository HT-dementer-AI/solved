# # 선택정렬의 시간 복잡도는 O(n^2)이므로 큰 값을 입력받았을때 속도가 느려서 시간초과가 나온듯 하다
# # 따라서 O(nlongn) 시간복잡도를 갖는 병합 정렬 또는 퀵정렬을 사용해야할것 같다
# # 아래는 퀵정렬을 이용한 정렬 방법이다.
# 아니 입력값을 받을때 오래걸려서 시간초과가 나는건 처음 본다
# 다음에 코딩할때 는 sys 모듈을 꼭 사용하자

# def quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot, tail = array[0], array[1:]

#     leftSide = [x for x in tail if x <= pivot]
#     rightSide = [x for x in tail if x > pivot]

#     return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)


# n = int(input())

# array = []

# for i in range(0, n):
#     array.append(int(input()))

# sortArray = quick_sort(array)

# for i in range(0, n):
#     print(sortArray[i])

import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(0, n):
    array.append(int(input()))

for i in sorted(array):
    print(i)

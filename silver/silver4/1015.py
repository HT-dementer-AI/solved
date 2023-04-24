# 문제 이해가 조금 난해했었던 문제이다.
# 예제 2를 예로 들자.
# 2 1 3 1 을 오름차순으로 정렬하면 1 1 2 3 이다.
# 이제 2 1 3 1 각각의 숫자가 정렬한 리스트에서 몇 번째 인덱스인지 출력하면 된다.
# 따라서 2 0 3 1 을 출력하면 정답이 된다.

num = int(input())

aList = list(map(int, input().split()))

sortList = sorted(aList)
resultList = []
startPoint = 0

for i in range(0, num):
    if(sortList.count(aList[i]) > 1):
        resultList.append(sortList.index(aList[i]))
        sortList[sortList.index(aList[i])] = -1
    else:
        resultList.append(sortList.index(aList[i]))


for i in range(0, num):
    print(resultList[i], end=" ")

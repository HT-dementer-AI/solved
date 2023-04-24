import sys
import datetime
input = sys.stdin.readline

array = list(map(str, input().split()))
array[1] = array[1][:-1]

dateDic = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
           "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
           "November": 11, "December": 12}

for i in range(len(array)):
    print(array[i])

# today = datetime.date(
#     year=int(array[2]), month=dateDic[array[0]], day=int(array[1]), hour=int(array[3]), minute=int(array[4]))

# print(today)

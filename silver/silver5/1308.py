import datetime
listToday = list(map(int, input().split()))
listFuture = list(map(int, input().split()))
today = datetime.date(listToday[0], listToday[1], listToday[2])
after1000 = datetime.date(listToday[0] + 1000, listToday[1], listToday[2])
future = datetime.date(listFuture[0], listFuture[1], listFuture[2])
d_Date = future - today
d_year = after1000 - today
if(d_Date < d_year):
    print(f"D-{d_Date.days}")
else:
    print("gg")

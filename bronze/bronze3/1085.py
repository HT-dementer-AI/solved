x1, y1, x2, y2 = map(int,input().split())

result = [x1, y1, x2 -x1, y2 - y1]

print(min(result))
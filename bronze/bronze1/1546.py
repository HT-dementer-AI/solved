n = int(input())
array = list(map(int, input().split()))

result = 0
mx = max(array)
for i in range(n):
    result = result + (array[i] / mx)

print((result/n)*100)

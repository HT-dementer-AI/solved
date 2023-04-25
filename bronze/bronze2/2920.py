string = "A"
array = list(map(int, input().split()))

for i in range(len(array)):
    string = string + str(array[i])

if(string == "A12345678"):
    print("ascending")
elif(string == "A87654321"):
    print("descending")
else:
    print("mixed")

array = []

while True:
    try:
        string = input()
        array.append(string)
    except:
        break

for i in range(len(array)):
    print(array[i])

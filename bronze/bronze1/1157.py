string = input()
string = string.lower()
array = []

a = list(string)
b = set(string)
b = list(b)

for i in range(len(b)):
    array.append(a.count(b[i]))

if(array.count(max(array)) == 1):
    print((b[array.index(max(array))]).upper())
else:
    print("?")

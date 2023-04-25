n = int(input())


def sum(string):
    k = 1
    result = 0
    for i in range(len(string)):
        if(string[i] == "O"):
            result = result + k
            k = k + 1
        else:
            k = 1
    return result


for i in range(n):
    string = input()
    print(sum(string))

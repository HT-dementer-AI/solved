n = int(input())
count = 0

def is_ck(string):
    element = string[0]
    result = []
    for i in range(len(string)):
        if(element != string[i]):
            result.append(element)
            element = string[i]
        else:
            continue
    result.append(element)

    if(len(result) == len(set(result))):
        # print(result)
        return True
    else:
        # print(result)
        return False




for i in range(n):
    string = input()
    if(is_ck(string) == True):
        count += 1

print(count)

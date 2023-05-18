result = 0

while (True):
    string = list(input().upper())
    result = string.count("A") + string.count("E") + string.count("I") + \
        string.count("O") + string.count("U")
    if (string == ["#"]):
        break
    # print(string)
    print(result)

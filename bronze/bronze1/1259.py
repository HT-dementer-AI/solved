while(True):
    value = input()
    if(value == "0"):
        break
    else:
        if(value == value[::-1]):
            print("yes")
        else:
            print("no")
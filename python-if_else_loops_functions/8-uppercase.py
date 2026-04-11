#!/usr/bin/python3
def uppercase(str):
    for i in str:
        temp = i
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            temp = chr(ord(i) - 32)
        print("{}".format(temp), end="")
    print("")

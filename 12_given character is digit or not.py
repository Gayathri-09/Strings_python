# program to check the given character is digit or not

def isDigit(s):
    for ch in s:
        if ch>='0' and ch<='9':
            print(ch,"is digit")
        else:
            print(ch,"is not digit")
print(isDigit("gayathri09 priya2002 me12"))

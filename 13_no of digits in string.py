# program to count number of digits in given string

def digitCount(s):
    count=0
    for ch in s:
        if ch>='0' and ch<='9':
            count=count+1
    return count
print(digitCount("gayathri0912 priya2002"))

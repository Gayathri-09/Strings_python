# program to count number of lowercase characters for the given string
'''
def lowerCaseCount(s):
    count=0
    for ch in s:
        if ord(ch)>=97 and ord(ch)<=122:
            count=count+1
    return count
s=input("enter a string to find number of lowercase char:")
res=lowerCaseCount(s)
print(res)
'''

#
'''
def lowerCaseCount(s):
    count=0
    for ch in s:
        if ch>='a' and ch<='z':
            count=count+1
    return count
print(lowerCaseCount("gayathri priya"))
'''

#

def lowerCaseCount(s):
    count=0
    for ch in s:
        if ch.islower():
            count=count+1
    return count
print(lowerCaseCount("gayathri priya"))

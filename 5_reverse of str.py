# program to reverse a given string
'''
def Reverse(s):
    l=len(s)
    l=l-1
    rev=''
    while l>=0:
        rev=rev+s[l]
        l=l-1
    return rev
s=input("enter the string:")
result=Reverse(s)
print("reverse of string=",result)
'''

#
def Reverse(s):
    l=len(s)
    l=l-1
    rev=''
    for ch in s:
        rev=ch+rev
    return rev
s=input("enter the string:")
result=Reverse(s)
print("reverse of string=",result)

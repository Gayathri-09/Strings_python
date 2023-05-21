# program to check given string is palindrome or not

def Palindrome(s):
    l=len(s)
    l=l-1
    rev=''
    for ch in s:
        rev=ch+rev
    return rev
s=input("enter the string:")
result=Palindrome(s)
if s==result:
    print(s,"palindrme")
else:
    print(s,"not palindrome")

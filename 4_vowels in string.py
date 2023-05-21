# program to count number of vowels in given string
'''
str=input("enter the string:")
c=0
for i in str:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        c=c+1
print("no of vowels=",c)
'''

# program to count number of vowels in given string using functions
'''
def Vowels(s):
    v=0
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            v=v+1
    return v
s=input("enter the string:")
result=Vowels(s)
print("no of vowels=",result)
'''

#
'''
def Vowels(s):
    v=0
    l="aeiou"
    for i in s:
        if i in l:
            v=v+1
    return v
s=input("enter the string:")
result=Vowels(s)
print("no of vowels=",result)
'''

#
'''
def Vowels(s):
    v=0
    l=['a','e','i','o','u']
    for i in s:
        if i in l:
            v=v+1
    return v
s=input("enter the string:")
result=Vowels(s)
print("no of vowels=",result)
'''

# program to count number of vowels specifically

def Vowels(s):
    a1=e1=i1=o1=u1=0
    l=['a','e','i','o','u']
    for ch in s:
        if ch=='a':
            a1=a1+1
        elif ch=='e':
            e1=e1+1
        elif ch=='i':
            i1=i1+1
        elif ch=='o':
            o1=o1+1
        elif ch=='u':
            u1=u1+1
    return a1,e1,i1,o1,u1
s=input("enter the string:")
a1,e1,i1,o1,u1=Vowels(s)
print("no of a=",a1)
print("no of e=",e1)
print("no of i=",i1)
print("no of o=",o1)
print("no of u=",u1)

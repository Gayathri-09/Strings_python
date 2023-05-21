# program to find the length of the string
'''
str=input("enter the string to find its length:")
print(str)
l=len(str)
print("length=",l)
'''

# program to find the length of the string without using len function

str=input("enter the string to find its length:")
c=0
for i in str:
    print(i,end=" ")
    c=c+1
print("length=",c)

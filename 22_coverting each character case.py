# program to convert each character case
# example: GaYaThrI -->  gAyAtHRi
'''
def case(s):
    l=len(s)
    s1=""
    for i in range(l):
        if ord(s[i])>=97:
            s1=s1+chr(ord(s[i])-32)
        else:
            s1=s1+chr(ord(s[i])+32)
    print(s1)
s=input()
case(s)
'''

def case(s):
    l=len(s)
    s1=''
    for i in range(l):
        s1=s1+chr(ord(s[i])^32)
    print(s1)
s=input()
case(s)
        

# program to generate all sub strings in given string

def substr(s):
    n=len(s)
    for i in range(n):
        s1=''
        for j in range(i,n):
            s1=s1+s[j]
            print(s1)
s=input()
substr(s)
        

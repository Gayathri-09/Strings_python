# find the count of values in the string
'''
def count(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    print(cnt)
s=input("enter the string")
count(s)
'''


def count(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(26):
        if cnt[i]!=0:
            print(chr(i+97),"-->",cnt[i])
s=input("enter the string")
count(s)


'''
def count(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        print(s[i],"-->",cnt[ord(s[i])-97])
s=input("enter the string")
count(s)
'''

'''
def count(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        if cnt[ord(s[i])-97]!=0:
            print(s[i],"-->",cnt[ord(s[i])-97])
            cnt[ord(s[i])-97]=0
s=input("enter the string")
count(s)
'''

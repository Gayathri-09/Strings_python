# program to print first non repeating character in a string
'''
def nonrep(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        if cnt[ord(s[i])-97]==1:
            print(s[i])
            break
    for i in range(26):
        if cnt[i]==1:
            print(chr(i+97))
            break
s=input()
nonrep(s)
'''


def rep(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        if cnt[ord(s[i])-97]==1:
            print(s[i])
            break
    for i in range(26):
        if cnt[i]>1:
            print(chr(i+97))
            break
s=input()
rep(s)


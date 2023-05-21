# maximum palindromic substring
'''
def palindrome(s):
    left=0
    right=len(s)-1
    mid=(left+right)//2
    for i in range(mid+1):
        if s[left]==s[right]:
            left=left+1
            right=right-1
        else:
            #print("no")
            return False
    #print("yes")
    return True
def substr(s):
    l=[]
    n=len(s)
    for i in range(n):
        s1=''
        for j in range(i,n):
            s1=s1+s[j]
            l.append(s1)
    return l
s=input()
l=substr(s)
n=len(l)
maxlen=0
ans=''
for i in range(n):
    if palindrome(l[i])==True:
        length=len(l[i])
        if length>maxlen:
            maxlen=length
            ans=l[i]
print(ans,maxlen)
'''


def large(s):
    l=len(s)
    maxlen=1
    index=0
    if l<2:
        print(s,l)
    else:
        for i in range(l):
            left=i-1
            right=i+1
            while left>=0 and s[left]==s[i]:
                left=left-1
            while right<l and s[right]==s[i]:
                right=right+1
            while left>=0 and right<l and s[right]==s[left]:
                left=left-1
                right=right+1
            length=right-left-1
            if length>maxlen:
                maxlen=length
                index=left+1
    print(s[index:index+maxlen],maxlen)
s=input()
large(s)

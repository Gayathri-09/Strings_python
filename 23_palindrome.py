#palindrome

def palindrome(s):
    left=0
    right=len(s)-1
    mid=(left+right)//2
    for i in range(mid+1):
        if s[left]==s[right]:
            left=left+1
            right=right-1
        else:
            print("no")
            return
    print("yes")
s=input()
palindrome(s)

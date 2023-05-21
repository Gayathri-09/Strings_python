# program to check given two strings are anagram

def anagram(s1,s2):
    cnt1=[0]*26
    cnt2=[0]*26
    n1=len(s1)
    n2=len(s2)
    for i in range(n1):
        cnt1[ord(s1[i])-97]+=1
    for i in range(n1):
        cnt2[ord(s2[i])-97]+=1
    if cnt1==cnt2:
        print("anagram")
    else:
        print("not anagram")
s1=input("enter the string")
s2=input("enter the string")
anagram(s1,s2)

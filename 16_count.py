# program to count vowels consonants digits and special characters

def count(s):
    vcount=0
    cons=0
    digits=0
    spchar=0
    vowels='aeiouAEIOU'
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vcount=vcount+1
            else:
                cons=cons+1
        elif ch>='0' and ch<='9':
            digits=digits+1
        else:
            spchar=spchar+1
    return vcount,cons,digits,spchar
s=input(" ")
cv,cc,cd,cs=count(s)
print("vowels=",cv)
print("cons=",cc)
print("digits=",cd)
print("spchar=",cs)

    

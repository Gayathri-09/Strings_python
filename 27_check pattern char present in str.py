#program to create a subtring that contains all elements in the pattern
#check whether all the pattern characters are there in the string and is minimum length

def enclose(s,p):
    sc=[0]*26
    pc=[0]*26
    pn=len(p)
    sn=len(s)
    start=0
    index=0
    minlen=sn+1
    count=0
    
    for i in range(pn):
        pc[ord(p[i])-97]+=1
    for j in range(sn):
        sc[ord(s[j])-97]+=1
        if sc[ord(s[j])-97]<=pc[ord(s[j])-97]:
            count+=1
        if count==pn:
            while sc[ord(s[start])-97]>pc[ord(s[start])-97] or pc[ord(s[start])-97]==0:
                if sc[ord(s[start])-97]>pc[ord(s[start])-97]:
                    sc[ord(s[start])-97]-=1
                start=start+1
            length=j-start+1
            if length<minlen:
                minlen=length
                index=start
    print(s[start:start+minlen],minlen)
s='maqxbbcvaxayzay'
p='aybxacy'
enclose(s,p)

                    
        

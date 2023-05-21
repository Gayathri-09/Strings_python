# read a user name and if string contains alphabets and digits return valid else return invalid
'''
def userName(s):
    if s.isalnum()==True:
         print("valid")
    else:
        print("invalid")
s=input("enter the string=")
userName(s)
'''

#
def userName(s):
    found=True
    for ch in s:
        if ch>='a' and ch<='z' or ch>='0' and ch<='9':
            continue
        else:
            found=False
            break
    if found==True:
        print("valid")
    else:
        print("invalid")
s=input("enter")
result=userName(s)
print(result)
            
    

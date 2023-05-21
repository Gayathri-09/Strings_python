# program to delete vowels from the given string
'''
def deleteVowels(s):
    result=''
    vowels='aeiouAEIOU'
    for ch in s:
        if ch not in vowels:
            result=result+ch
    return result
#print(deleteVowels("vardhaman"))
s=input("enter the string")
r=deleteVowels(s)
print(r)
'''


# program to delete vowels from the given string and count number of vowels deleted

def deleteVowels(s):
    result=''
    vowels='aeiouAEIOU'
    count=0
    for ch in s:
        if ch not in vowels:
            result=result+ch
        if ch in vowels:
            count=count+1
    return result,count
#print(deleteVowels("vardhaman"))
s=input("enter the string")
r,c=deleteVowels(s)
print("string without vowels",r)
print("no of vowels deleted",c)

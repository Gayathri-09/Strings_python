# program to check the given character is vowel or consonant

def checkVowelsCons(ch):
    vowels='aeiouAEIOU'
    if ch.isalpha():
        if ch in vowels:
            print(ch,"is vowel")
        else:
            print(ch,"is consonant")
    else:
        print("it is not alphabet")
ch=input("enter the string")
checkVowelsCons(ch)


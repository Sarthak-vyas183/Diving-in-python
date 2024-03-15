# # Practice question only list , touple , sets , Dictionary : 
# #  question 1 :  print a String reverse its length , UpperCase , LowerCase , and copy into another String 
#     # uppercase
from networkx import volume

str = "shreemati radha rani ki jay"
print(str.upper())
str2 = "SARTHAK VYAS"
print(str2.lower())
print(len(str))

# revese of a string : 
b  = "" #empty string
for i in range(len(str)-1 ,-1,-1): 
    b += str[i]

print(b)

# question first completed : 
# Arrenge the string charactor such that lowercase latter come first in new string
a = "sHrEE mAti rAdhA RANi kI JaY"
b = ""
for i in a:
    if i.islower():
        b+=i 

for i in a:
    if i.isupper():
        b+=i 
print(b)
   

# 3) count the latter , digit and special symbole : 
givenStr = "P@#yn26at^&i5ve"
char = 0
num = 0
spchr = 0
for i in givenStr:
    if i.isalpha():
        char=char+1
    elif i.isdigit():
        num = num + 1
    else:
        spchr = spchr+1

print("Total count of char digit and special char")
print(f"Character: {char} \nDigit: {num} \nSpecial character: {spchr}")

# 4) count vowel from given string : 
def volconst(str3 , vol , const): 
    vowel = vol 
    const = const
    for i in str3:
        if i in 'aeiouAEIOU':
            vowel += 1
        else:
            const += 1
    return vowel, const

a = "shreemati radha rani ki jay"
print(volconst(a,0,0)) 


# 5) check the string is pallindrom or not - pallindrom means --- sidha or ulta reading same 'jiyaji'
str5 = input("Enter string")
str6 = ""
for i in range(len(str5)- 1,-1,-1):
    str6 += str5[i]

if str6 == str5 :
    print("String is pellindrom ")
else :
    print("String is not a pellindrom")




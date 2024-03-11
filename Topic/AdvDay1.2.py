# how we use return function 

def evenodd(a):
    if a%2 == 0:
        return ("even")
    else:
        return ("odd")
    
result = evenodd(15)
print(result)       #this is was how we use return 


# String 
a = "shreemati radha rani ki jay"
print(a[5])

# String slicing 
print(a[0:9])    # 0 index to 9th index tak ki String print hogi
print(a[9:])     # 9 index to end index tak ki string print hogi 
print(a[0:9:2])   # here 2 is steps it mean ek index  chhod ke chalega code 
b = "s0a0r0t0h0a0k "    # for this situation we use steps
print(b[0:len(b):2])    #len() function use to know the length of a string 
print(len(b))



str = "sarthak vyas"

if "vyas" in str :    # "in" keyword is use to check that string  is exist in main string or not
    print(True) 
else:
    print(False)

for i in range(7,len(str)):
    print(str[i]) 



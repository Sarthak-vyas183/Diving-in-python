# Tody topic : Function , String , list , touple , Dictionary ,Sets : 
# start of 1 . Function 
# Function is reuseable block of code : 
# how to define a function 
def sum(a , b , d = 40):            #def key workd function name sum : thats all 
    sum = a + b + d          #a and b is parameter define 
    print(sum)                # here 40 is default parameter 
                             # (d = 40) syntax of default parameter
sum(2,5)                          # 2 and 5 are  argument 
sum(10,30,60)               # argument 60 overlap parameter d = 40 to d = 60
sum(d=30 , a=50, b=20)          #this called keyword argument

def evenodd(a):
    if a%2 == 0:
        print("even")
    else:
        print("odd")    

evenodd(12)
evenodd(13)
evenodd(14)
evenodd(15)
evenodd(16)
evenodd(17)
evenodd(18)
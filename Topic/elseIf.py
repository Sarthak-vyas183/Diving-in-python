# light = input("enter traffic ligth color ")
# if(light == "red"):
#     print("Stop : ")
# elif(light == "yellow"):
#     print("Wait : ")
# elif(light == "green"):
#     print("Go ! fast")

# marks = int(input("enter your marks : "))
# if(marks >= 90):
#     print("grade : A+")
# elif(marks >= 80 and marks < 90):
#     print("grade : B")
# elif(marks >= 70 and marks < 80):
#     print("grade : C")
# elif(marks >= 50):
#     print("grade : D")
# elif(marks >= 33):
#     print("grade : E")
# else:
#     print("fail : Try again !")

#practice Questions :

# WAP to check the entered number by user is even of odd 
# num = int(input("enter the number"))
# if(num%2==0):
#     print("entered number is even")
# else: 
#     print("enterd number is Odd : ") 

#WAP to find greatest of 3 numbers entered by the user : 
# first = int(input("enter first Number : "))
# second = int(input("enter second Number : "))
# third = int(input("enter third Number : "))
# if(first > second):
#     if(first  > third):
#         print("first number ",first," is greater in all ")
#     else:
#         print("Third number",third," is greater : ")
# elif(first > third):
#     print("second number ",second," is greater") 
# elif(second > third):
#     print("second number ",second," is greater") 
# else:
#     print("third number ",third," is greater :")

#that was very conlex code so see the easy solution

# if(first > second and first > third):
#     print("first number ",first," is greater in all ")
# elif(second > third and second > first):
#     print("second number ",second," is greater")
# elif(third >first and third>second):
#     print("third number ",third," is greater :")

#WAP a program to check the number is multiple of 7 or not
# num = int(input("enter the number"))
# multi = num%7
# if(multi == 0):
#     print(num," is multiple of 7")
# else:
#     print(num," is not multiple of 7")
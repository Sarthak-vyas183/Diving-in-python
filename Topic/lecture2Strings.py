# type of String is : 
# str = "sarthak"
# str2 = 'sarthak'
# str3 = '''nachiketa'''
# print(str,str2,str3)

#line change \n
# str1= "hello my name is sarthak vyas\nStudent of computer Science."
# str1= "hello my name is sarthak vyas\tStudent of computer Science." 
# print(str1)

#using len(str) length function we can identify length of a string : 
#str1 ="hello my name is sarthak vyas\nStudent of computer Science."
# length = len(str1)
# print(length)
#print(len(str1))  second way 

#indexing
# string = "hey i am studing at apna college"/
#print(string[0])
# string[0] = string[9]  not allow
# print(string)


#slicing - Accessing part of a string :

#str1 = "hello my name is sarthak vyas Student of computer Science."
# print(str1[0:6])   dont need to write slice keyword
# print(str1[0:])
#Nagetive indexing
# print(str1[-4:-2])
# print(str1[-58:-53])

#String Functions
#str.endswith(substring) return true is string end with substring 
#str.capitalize()    it capitalize first charactor
#str.replace(old,new)  replace all the occurrence of old with new 
#str.find(word)   return first index of 1st occurrence 
#str.count("am")  count the occurrence of substring in string
  #use of String function
# str1 = "hello my name is sarthak vyas Student of computer Science"
# print(str1.endswith('nce'))
#print(str1.capitalize())
# print(str1.replace("Science","Application"))
#print(str1.find("o"))
# print(str1.count("sarthak"))

# Que : write a program to take input from user an print its length
# name = input("enter your name ")
# length = len(name)
# print("length of your name is : ",length)

# Que : WAP to find occurrence of $ in the string  :
# str = input("inter  a state which contain $ sing : ")
# print(str.count("$"))


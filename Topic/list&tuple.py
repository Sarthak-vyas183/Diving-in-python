# student = ["sarthak ","85%","MCA2310013" , "MCA"]
# student[0] = "Nachiketa"
# print(student)
# print(type(student[0]))

#method or function in list : 
Mo = [9, 3, 0, 2, 6, 9, 5, 6, 8, 9]
# Mo.append(3)
# Mo.sort()
# print(Mo)/

#for reverse sorting : 
# Mo.sort(reverse=True)
# print(Mo)

#reverse method :
# Mo.reverse()   #this function reverse the  whole string : 
# print(Mo)

#insert method : 
#Mo.insert(2,7)   # insert(idx,element)

# Mo.remove(9)  # it remove first occurence of elemetn
# print(Mo)

# Mo.pop(3)   # pop the element from the list list.pop(idx)
# print(Mo)




#Tuples in Python : Tuples are immutable like string and assignment is not allowed : 
# tup = ("string",45)
# print(tup)
# print(type(tup))

#methods in tuples : 
#tup = ("sarthak",45,98.5,9,3,0,2,6,9,5,6,8,9)

# print(tup.index(9))   #return the occurrence of element
#print(tup.count(9))

#WAP to ask user to enter three fevorate movi name & store them in a list 
# list = []
# F = input("enter movie name")
# S = input("enter movie name")
# T = input("enter movie name")
# list.append(F)
# list.append(S)
# list.append(T)
# print(type(list))
# print(list)

#WAP to check a list contain Palindrome element
# list = [1,2,3,2,1]
# list2 = list.copy()
# list2.reverse()
# print(list2)

# if(list2 == list):
#     print("list is palindrom:")
# else:
#     print("not palindrom")

#WAP to count number of student with A grade in the following tuple
 #["C","D","A","A","B","B","A"] 
# tub = ("C","D","A","A","B","B","A","A") 
# print("Number of students in following tuple :", tub.count("A"))

#store the above value in list and sort this A to D
# tub = ["C","D","A","A","B","B","A","A"] 
# tub.sort()
# print(tub) 


#Second lecture on list - 
# list is versatile mutable data structure that allow you to store collective item : 
a = [2,3,6,5,4,8,2,2]
a[2] = 30
print(a[0:3])

for i in range(0,len(a)):
    print(a[i])
# mehtod of lists in python
# Method	Description
    
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()   	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
a.append(45)  
b = a.copy()
# a.clear()
a.insert(2,99)
a.pop(2)
a.remove(2)
a.remove(2)
a.remove(45)
a.reverse()
a.sort()
res = a.count(2)
print(a)
print(res)   

# Tuple 
# tuple is like list but it is immutable and can not be change once it is made
#  you have to use () to create touple : 
z = tuple(a)        # tuple() function is used to 9565714102
print(z)            
#tuple unpacking 
tpl = (2,5,8,9)
b,c,d,e = tpl        # in we unpack the tuple b=2 , c=5, d=8, e=9   
print(d)             

# Sets
# sets is also collection of items must be unique but it is unordered and unchagable
# you have use {} to make a set

set = {"sarthak" , "vyas","nachiketa" , "radha"}

# for i in range(0,len(set)):
#     print(set[i])             wrong way ro write loop in set because set in unorder indexing are not allow
for i in set:
    print(i)      #unordered



# new topic Dictionary 
#Dictionary is also like list it is mutable 



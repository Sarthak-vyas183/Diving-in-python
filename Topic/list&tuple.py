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
tub = ["C","D","A","A","B","B","A","A"] 
tub.sort()
print(tub)


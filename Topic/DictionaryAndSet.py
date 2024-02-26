# dictionary are used to store data value in Key:value pair
# we can also create list and touple in a dictionary : 
info = {
    "name" : "sarthak",
    "age" : 25,
    "address" : "bhopal",
    "country" : "india",
    "learnig" : "coding",
    "subject" : ["java","python","c++","Ejs"] , 
    "topic" : ("dict", "touple" , "list"),
    "is_adult" : True
    
} 
# print(info)
# print(type(info))
# print(info["name"])
# we also can assign new value to the key : 
info["name"] = "Vedant"
info["sur"] = "Vyas"
# print(info["name"] , info["sur"])


# we also create a null dictionary : 
null_dict = { }
# print(null_dict)
null_dict["name"] = "Nachiketa"
null_dict["age"] = 12
null_dict["course"]= "kad-Upnishad"
# print(null_dict)

# nested dictionary : 
nested_dict = {
  "name" : "Gargi", 
  "age" : 23 , 
  "subject" : {
      "phy" : 96,
      "ches" : 45,
      "math" : 75 
},
  "branch" : "CS/IT"
}
# print(nested_dict)
# print(nested_dict["subject"]["ches"])
# print(nested_dict["subject"]["math"])


# print(len(list(info.keys())))

# use of function or method 
# dict.keys()
# print(nested_dict.keys())
# print(nested_dict.values())
#print(nested_dict.items())  return all the key value pair in touple format 
# print(nested_dict.get("name")) # return all value according to the key : 
info.update({"city" : "delhi"})   #insert the specificed item to the dictonary  
# print(info)

# set is a collection of unordered items 
# and each element in the set must be unique and immutable 
# just because we can't store list and touple in sets 
Set_collection = {1,2,2,2,"hello","world","world"} 
# print(Set_collection)
# print(type(Set_collection))
collection = set () # to create empty set ; syntax 
# print(collection)

# method or fuction in sets : set.add(el)
collection.add(2)
collection.add(5)
collection.add(2)
collection.remove(2)
collection.clear()
# print(collection)

set1 = {1,2,3,4}
set2 = {2,3,4,5,6}
# print(set1.union(set2)) #(1,2,3,4,5,6)
# print(set1.intersection(set2)) #(2,3,4)


# Practice Questions : 
# Que :1. store the following words and meaning  in dictionary
dict = {
    "table" : ["a piece of furniture" , "list of fact and figure"],
    "cat" : "a small animal"
}
# print(dict) 

# que :2. you are given a list of subject for student . Assume one classroom is require for one subject how many classes are  needed by all student .
list = ["python","java" , "c++","python","javascript","java","python","c++","c"]
# print(len(set(list)))

# WAP to enter marks of 3 subject from the user and store them in dictionary start with and empty dictionary and add one by one use subject as key and marks as value 
marks = {}
chem = input("enter the marks of chemistry ")
phy = input("enter the marks of physics ")
math = input("enter the marks of Math ") 
marks["chemistry"] = chem
marks["physics"] = phy
marks["Math"] = math 
print(marks)
if(int(marks["chemistry"]) < 33):
    print("Failed in chemistry") 

if(int(marks["Math"]) < 33):
    print("Failed in Math")
if(int(marks["physics"]) < 33) :
    print("Failed in physics")
total = int(marks["chemistry"]) + int(marks["Math"]) + int(marks["physics"])
if(total <= 99) :
    print("Completly Failed") 

# que - figure the  way to store 9 & 9.0 in set 
value = {
    ("int" , 9),
    ("float" , 9.0)       
   }
print(value)

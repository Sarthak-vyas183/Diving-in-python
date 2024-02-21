# dictionary are use to store data value in key:value pair
# all type of value are acceptable in dictionary : 
# Weal also can store list and touple in dictionary :
info  = {
   "key" : "value",
   "name": "sarthak",
   "learning":"python",
   "age":22,
   "is_adult":True,
   "marks":94.3,
   "subjects":["python","java","C","js"],
   "topic":("dic","set")
}
#print(info)
#we can't access the dict key throught index (there is no index)
# dict are unordered and mutable and don't allow duplicate value
info["name"] = "vedant"             # because dict are mutable 
info["surname"] = "sharma"         #we can add new key value 
print(info["name"],info["surname"])
print(info["age"])
print(info["marks"])
print(info["subjects"])


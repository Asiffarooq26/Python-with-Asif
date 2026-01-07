#Sets
# my_set={25,87,25,87}
# # print(my_set)
# # my_set.add(985)
# my_set.update([1, 2,3,2,5])
# print(my_set)
# # my_set.remove(96)
# # my_set.discard(960)
# # my_set.clear()
# my_set.pop()
# print(my_set)
set1 = {1, 2, 3,4}
set2 = {3, 4, 5}
# print(set1.union(set2)) #
# print(set1.intersection(set2)) # common
# print(set1.difference(set2)) # in set1 not in set2

# my_list=["Akash","Harvinder","Asif","Ajaz","Om Shukla","Rameshwar Patil"]
# for i in my_list:
#     print(i)

#Dictionary
mydict={"name":"Rameshwar",
        "city":"Maharashtra",
        "class":"B.com"}
print(type(mydict))
mydict["country"]="India"
mydict["class"]="M.com"
# print(mydict["name"])
# print(mydict["city"])
# mydict["name"]="Om shukla"
# print(mydict["name"])
# city=mydict.get("city")
# print(city)
print(mydict)
# mydict.pop("class")
# mydict.popitem()
# mydict.clear()
# print(mydict)
# print(mydict.get("country"))
# print(mydict.keys()) #Displays only Keys
# print(mydict.values())#Displays only values
# print(mydict.items()) #Displays Key value pairs
# print(mydict)
# mydict.update({"name":"Ajaz"})
# print(mydict)
# for key in mydict:
#     print(key)

# for asif in mydict.values():
#     print(asif)

# for key,value in mydict.items():
#     print(key,value)

student={
    "name":"Garvit Mathur",
    "marks":[50,80,90],
    "info":{
        "city":"Jaipur",
        "age":22,
        "friend":{
            "name":"Manish",
            "city":"Srinagar"
        }
    }
}
print(student["info"]["friend"]["name"])
print(student["info"]["friend"]["city"])
# print(student['info']['city'])

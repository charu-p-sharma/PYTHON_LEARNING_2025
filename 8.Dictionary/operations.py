# Creation 
my_dict1={
   "name":"charu",
   "age":23,
   "marks":95.6,
   "favs":["cherry","strawberry"]
}
print(my_dict1)

# OPERATIONS ON DICTIONARY
# Adding a pair elements to dictionary
my_dict2={
    "fruits":["apple","mango","banana"]
}
my_dict2['Price']=200
print(my_dict2)

# Updating elements in dictionary
my_dict3={
    "name":"python",
    "version":3.5,
}

# adding new pair of element
# my_dict3["updated_version"]=3.7
# print(my_dict3)

# updating the existing pair of element
my_dict3["version"]=3.7
print(my_dict3)


# Deleting from Dictionary
my_dict4={
    "name":"python",
    "version":"3.9",
   "Use_case":["AI","ML","DA"]
}
print(my_dict4)
del my_dict4["version"]
print(my_dict4)
# GET METHOD 
# TO FETCH DATA FROM DICTIONARY
profile={
    "name":"ram",
    "age":25,
    "salary":45000.0
}
Age=profile.get("age")  #to only display the value
Age_txt=profile.get("age_1","Age not found") # to display value or a msg if value not found
print(Age)
print(Age_txt)

# TO FETCH KEYS FROM DICTIONARY
Keys=profile.keys()
print(Keys) # as it returns in list in tuple 
print(list(Keys))

# TO FETCH VALUES FROM DICTIONARY
Values=profile.values()
print(Values)

# TO FETCH ALL ITEMS FROM DICTIONARY
all_items=profile.items()
print(all_items)

# POP METHOD
popped1=profile.pop('age')
popped2=profile.pop('age1',"Age Not found")
print(popped1)
print(popped2)

# POP ITEM METHOD (pops the last item from the dictionary)
popped_i=profile.popitem()
print(popped_i)
print(profile) 

# CLEAR METHOD
print(profile) 
clear_dict=profile.clear()
print(clear_dict)
print(profile) 
"""
WHAT WAS THE NEED FOR LSITS AND TUPLES ?

Example:Storing student information in huge scale
name="charu
age=23
marks=95.5
gender="female
...etc

If you see to store different values different variables had to be declared
of different types , so python gives the solution to solve this issue.

CHARACTERISTICS OF LIST
- ordered
- mutable 
- dynamic
- heterogenous (diff. data types)
"""

# WAYS TO DECLARE LIST
# square brackets
my_list1=[1,2,3,"hello",True]
print(my_list1)
# list constructor
my_list2=list((1,2,3,"hello",True))
print(my_list2)
# list comprehension and range()


# WAYS TO UPDATE ITEMS IN LIST
# normal indexing 
my_list3=[1,2,3]
my_list3[0]="CHARU"
print(my_list3)
# slicing
my_list4=[1,2,3,4,5]
my_list4[0:3]="CHARU","PANKAJ",100
print(my_list4)

# CONCATINATION IN LIST
my_list5=[1,2,3]
my_list6=[4,5,6]
result_list=my_list5+my_list6
print(result_list)

# REPEATATION IN LIST
my_list7=[1,2,3]
repeat_list=my_list7*2
print(repeat_list)

# REPEATATION IN LIST

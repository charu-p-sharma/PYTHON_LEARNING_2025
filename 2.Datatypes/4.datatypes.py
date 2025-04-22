"""
Numeric datatype
1. int - whole number
2. float - decimal number
3. complex - real and imaginary like 3+4j
"""
a=10
b=1.2
c=3+4j
print(a,b,c)
print(type(a),type(b),type(c))


"""
Boolean datatype
true/false
"""
a= True
b= False
print(a,b)


"""
None datatype
- It means there is no value assigned currently to it.
- However i may assign a value in the future.
- It wont throw any errors.
"""
result = None
print(result)
result = 1
print(result)


"""
Sequence Datatypes
1.string 
2.list
3.tuple
"""

"""
Strings 
- Anything written inside "" or ''
- They are immutable (cannot be changed later)
- You cannot change but update strings.
"""
text= "this is a string"
print(text)
print(type(text))


"""
Lists
- It is a collection of data.
- Written inside [] brackets
- They are mutable
"""
my_list=["d1","d2","d3"]


"""
Tuple
- It is a collection of data.
- Written inside () brackets
- They are immutable
"""
my_tuple=("d1","d2","d3")


"""
Sets Datatype
1. Sets
2. Frozen Sets
"""

"""
1. Sets
- It only returns unique values
- Unordered collection of unique items
- They are mutable
- Data can be modified here in sets.
- Written inside {} brackets
"""
set={1,2,3,3,4,5,1,1,1,1,3,3,3,4,4}
print(set)


"""
2. Frozen Sets
- It only returns unique values
- Unordered collection of unique items
- They are immutable
- Data cannot be modified here in frozen set
- Written inside {} brackets
"""
frozen_set={1,2,3,3,4,5,1,1,1,1,3,3,3,4,4}
print(frozen_set)


"""
Mapping Datatypes
1. Dictionary - key value pair
"""

"""
Dictionary 
- Key value pair separated by semicolon
- Written inside {} brackets
- But we store data in pairs
- Any datatype could be used to store the value here.
"""
person={"name":"charu","age":23,"height":5.2}
print(person)

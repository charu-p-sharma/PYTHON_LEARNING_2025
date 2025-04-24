"""
Strings and Characters
- are the sequence of characters used to store or represent any text 
What are strings
- anything inside '' or "" or ''' ''' or """ """
- ''' ''' or """ """ are used to store multi line texts
- strings are immutable, the strings value can be updated but not changed 
- strings are indexed
- strings are iterable
"""

# STRINGS ARE IMMUTABLE 
name ="Charu"     #-> original value
name = "Sharma"   #-> updated value 

# INDEXING IN STRING
a = "python"
""" 
POSTIVE INDEXING(LEFT->RIGHT)
p-> 0
y-> 1
t-> 2
h-> 3
o-> 4
n-> 5
"""
print(a[0])
""" 
NEGATIVE INDEXING(RIGHT->LEFT)
p-> -6
y-> -5
t-> -4
h-> -3
o-> -2
n-> -1
"""
print(a[-5])


# STRINGS ARE ITERABLE
lang_name="python"
for i in lang_name:
    print(i)
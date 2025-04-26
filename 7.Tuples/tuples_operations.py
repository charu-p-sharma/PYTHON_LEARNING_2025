# TUPLES
"""
CHARACTERISTICS OF TUPLES
- immutable
- heterogenous (diff. data types)
- syntax = use ()
"""

"""
NOTE: Use tuples only when you dont want to change the data after creating.
Example : Bank details , account numbers , DOB , Name
"""

a= 10,20,30
print(type(a))  #this gives tuple only but avoid declaring data like this

b=(10,20,30,40)
print("This is a tuple",b)

c=()
print("This is a empty tuple",c)


"""
OPERATIONS ON TUPLE
- len()
- min and max
- count()
- index()
- sorted()
"""

# ACCESSING TUPLE ELEMENTS
d=(1,2,3)
print(d[1])

"""
This throws error as tuples are immutable
e=(1,2,3)
e[1]="hi"
print(e)
"""

# SLICING 
f = (1,2,3,4,5,6)
print(f[0:4:1])


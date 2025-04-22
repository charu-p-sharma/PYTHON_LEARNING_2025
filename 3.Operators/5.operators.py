"""
Arithmetic operator
"""
print("Arithmetic operator")
x=10
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)  # division - gives exact value
print(x//y) # floor division - removes decimal and gives round off value
print(x%y)  # modulus - returns remainder
print(x**y)  # exponential 

"""
Comparison operator
- To comapre values 
- Output is in boolean outputs
"""
print("comparison operator")
a=10
b=20
print(x==y)  # to check if values are equal
print(x!=y)  # to check if values are notequal
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


"""
Logical operator
- To comapre values 
- Output is in boolean outputs
- and --> all conditions should be true
- or  --> atleast one condition should be true
- not --> reverses the value
"""
print("Logical operator")
age=20
is_adult = True
print(age>18 and is_adult)
print(age>23 or is_adult)
print(not age)


"""
Assignment operator
=
+=
-+
*=
/=
"""
print("Assignment operator")
p=10
print(10)
p+=5  # p=p+5
p-=5  # p=p-5
p*=5  # p=p*5
p/=5  # p=p/5
print(p)



"""
Identity operator
- It is used to compare the memory location of 2 objects
- is -> returns true if memory location is same 
- is not -> returns false if memory location is different 
"""
print("Identity operator")
a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(b is c)


"""
Membership operator
- It is used to check if a value exists in a sequence or not.
- in
- not in
"""
print("Membership operator")
veggies=["pea","chilli","tomato"]
print("pea" in veggies)
print("potato" not in veggies)
print("potato" in veggies)


# Summary
"""
arithmetic - math calculations
comparison - compare values
logical - combine
assignment - assign values
identity - object memory location
membership - value exist in sequence
"""

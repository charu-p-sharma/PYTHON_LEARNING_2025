"""
Control Statements
- It controls the flow/execution of the program
- conditional - if,else,elif
- for while else suite
- nested
- infinite loop
- pass 
- continue 
- break
- assert return
"""

"""
If you see the below code, 
you can see that we do not have any control 
over the flow or the execution here.
"""
radius = 7
area_circle= 3.14* radius*radius
print("Area of circle",area_circle)


# IF statement
"""
syntax
if (condition):
    statements
"""
print("IF statement")
age= int(input("Enter your age="))
if age>18:
    print("You are eligible to vote")


# Indentation
print("Indentation Representation")
age1= int(input("Enter your age="))
if age1>18:
    print("You are eligible to vote")
print("This is not under if statement,so it is independent and always printed")


# ELSE statement
"""
syntax
if (condition):
    statements
else:
    statements
"""
print("ELSE statement")
age= int(input("Enter your age="))
if age>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



# ELIF statement
"""
syntax
if condition:
    statements
elif condition:
    statements
else:
    statements
"""
print("ELIF statement")
age= int(input("Enter your age="))
if age>=18:
    print("You are eligible to vote")
elif age<18:
    print("You are not eligible to vote")
elif age<0:
    print("Enter a proper age!")
else:
    print("Invalid input")
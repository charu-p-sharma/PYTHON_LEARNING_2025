"""
Arithmetic Calculator
Create a program that accepts values and inputs from user
to perform any arithmetic operations and display then output.
"""

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation= input("Choose which operation to perform among +,-,*,/,//,% :")

if operation =='+':
    sum=num1+num2
    print("The total sum is",sum)
elif operation == '-':
    diff=num1-num2
    print("The differnce is",diff)
elif operation == '*':
    mul=num1*num2
    print("The product is",mul)
elif operation == '/':
    div=num1/num2
    print("The division value is",div)
elif operation == '//':
    floor_div=num1+num2
    print("The floor division is",floor_div)
elif operation == '%':
    mod=num1%num2
    print("The modulus value is",mod)
else:
    print("Invalid input")


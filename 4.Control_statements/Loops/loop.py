"""
Loops -  are the conditional statements that are repeated multiple times
- while loop
- for loop
"""

"""
while loop
- It is executed until it is true
syntax
while conditon:
    statements
"""
num1=5
while num1<=5:
    print("Number is a positive number")
    num1=num1+1

    

"""
for loop
- It is used to do iteration over sequences
syntax
for variable in sequence:
    statements
"""
list1=[1,2,3,4,5]
for i in list1:
    print(i)


"""
infinite loop
"""
# while True:
#     print("Infinite loop")


"""
Range function
range(start,stop,step)
start - what to start from
stop - till what (stop is exclusive)
step - interval or by what to skip (by default it takes 1)
"""
a=list(range(1,10,1))
print(a)
b=tuple(range(1,11,1))
print(a)


"""
Nested Loops
"""
for i in range(1,3):
    for j in range(3,6):
        print(f'{i},{j}')
"""
The f before the string tells Python: “this is a formatted string.”
Anything inside {} will be evaluated and inserted into the string.
"""


"""
break
- to stop the loop immediately if a certain condition is met
"""
for number in range(1,10,1):
    if number ==5:
        break
    print(number)



"""
continue
- to skip the current interation and move to the next
"""
for number1 in range(1,10,1):
    if number1==5: # It will skip the number 5
        continue
    print(number1)


"""
pass
- used as a dummy placeholder
- it does nothing 
- but allows the program to run
- example: I wrote a block of code and suppose i dont want to write the main logic today 
           so instead of leaving a program incomplete i will use pass statement
           so that my program runs irrespective of the main logic that i had to write so
           basically it is allows to run instead of blocking.
"""

for number2 in range(1,10,1):
    if number2==5: # Here i want to write a logic to perform for this conditon
        pass # so i have used pass which will allow the program to run and in future when i want i can write the logic here
    print(number2)
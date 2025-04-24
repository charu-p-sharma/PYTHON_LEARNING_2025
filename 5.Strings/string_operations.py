""" 
OPERATIONS IN STRING
- len
- slice
- index 
- product
- concatination
- checking
"""

# len() 
str1="python"
print(len(str1))
str2="python is a language"
print(len(str2))


"""
PROBLEM:Accept password from the user and validate if the length
of the password is greater than 5 characters then it is accepted orelse 
not accepted
"""
password=input("Enter the password:")
if len(password)>5:
    print("Password accepted")
else:
    print("Password not accepted")


# SLICING IN PYTHON
# string[start:stop:step]
str3="charu sharma"
print(str3[0:5:1])

""" if nothing is passed then it takes entire string
start- 0
stop- length of string
step- +1
"""
print(str3[::])
""" if negative step is passed then it takes from the end of string
start- -1
stop- starting of string
step- -1
"""
print(str3[::-1])

# normal numbers's product
number=10
print(number*20)  
# string repeated 20 times
number="10"
print(number*20)
# normal number's exponential value
number=10
print(number**20)
# exponential value of string is not possible
# number="10"
# print(number**20)


# CONCATINATION
# strings can only be concatinated with strings only.
name1="charu"
name2="sharma"
fullName=name1+name2
print("Hi",fullName)


# CHECKING
"""
- membership in operator
- membership not in operator
"""

"""
PROBLEM: Ask user for input and return if it is valid or not 
"""
user_email=input("Enter the email:")
if "@" in user_email:
    print("Valid Email")
else:
    print("InValid email")
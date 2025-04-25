# LOWER CASE
str1= "THIS IS PYTHON"
print(str1.lower())
str2=input("Enter your name:").lower()
print(str2)

# UPPER CASE
str3= "this is python"
print(str3.upper())
str4=input("Enter your name:").upper()
print(str4)

# CAPITALIZE (only first letter of string is capital)
str5=input("Enter your name:").capitalize()
print(str5)

# TITLE (first letter of all characters of string is capital)
str6=input("Enter your name:").title()
print(str6)

# SWAPCASE (capital becomes and lower becomes capital)
str7=input("Enter your name:").swapcase()
print(str7)

# SEARCHING STRING METHOD
# - It returns the first occurence of that character in the string
text1="python programming"
print(text1.find("p"))  # first aoccurance of character p

# REPLACING STRING METHOD
text2="python programming"
print(text2.replace("python","javascript"))  

# SPLITTING STRING METHOD
str8="a,b,c"
print(str8.split(",")) #returns a list of those separated strings

# JOINING STRING METHOD
str9=["a","b","c"]
str10=",".join(str9)
print(str10)

# CHECKING METHOD (startsWith)
str11="Python"
print(str11.startswith("P"))

# CHECKING METHOD (endswith)
str12="Python"
print(str12.endswith("N"))

# CHECKING METHOD (isalpha)
str13="Python"
print(str13.isalpha())

# CHECKING METHOD (isdigit)
str14="Python"
print(str14.isdigit())

# CHECKING METHOD (isalphanumeric)
str14="Python12"
print(str14.isalnum())

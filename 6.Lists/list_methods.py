# ALIAS
list_1=[1,2,3]
list_2=list_1

list_2[0]="charu"
print("list 1",list_1,"list 2",list_2)


# COPY
list_3=[1,2,3]
list_4=list_3.copy()
list_4[0]="charu"

print("list_3",list_3,"list_4",list_4)


# APPEND METHOD
#  data gets added to the last place of the digit by default.
a=[1,2,3]
a.append(4)
print(a)

# EXTEND
b=[1,2,3]
c=[4,5,6]
b.extend(c)
print(b)

# INSERT
# syntax = insert(position,data)
d=[1,2,3]
d.insert(0,"hi")
print(d)

# REMOVE (just pass the data to remove)
e=[1,2,3]
e.remove(3)
print(e)

# POP (just pass the indexed number of data to remove)
f=[1,2,3,4]
f.pop(3)
print(f)

# CLEAR (to remove the elements from the list and return empty list)
g=[1,2,3]
g.clear()
print(g)

# INDEX (to know the index value of the element)
h=[1,2,3]
indexed_num=h.index(3)
print(indexed_num)

# COUNT (to count how many times a particular data occurs in the list)
i=[1,2,3,4,1,1,1,1,1,1,3,2,4,7,7,8]
count_num=i.count(1)
print(count_num)

# SORT
j=[9,4,7,1,2,0,4,5,3,8,7,9]
sorted_list=j.sort()
print(j)

# REVERSE
k=[1,2,3,4,5]
k.reverse()
print(k)

# MIN AND MAX
l=[1,2,3,4,5]
print(min(l))
print(max(l))

# COMMON ELEMENTS IN SET
m=[1,2,3,4,5,6]
n=[1,2,8,9]
# convert the lists to set
s1=set(m)
s2=set(n)
# find the common using intersection
o=s1.intersection(s2)
print(o) # to just return the data as a set
print(list(o)) #to return data as a list

# NESTED LIST
p=[1,2,3]
q=[1,2,3,4,5,[6,7,8],]
print(q)

# RANGE FUNCTION IN LIST
"""
range()
start
stop
step
"""
r=list(range(0,20,1))
print(r)

# LIST COMPREHENSION
"""
[expression for item in iterable if condition]
exprression = x*2
iterable = range(1,10,1)
condition - its optional
"""
# old traditional code to print sqaure of numbers from 1-10 in a list
squares=[]
for i in range(0,11,1):
    squares.append(i ** 2)
print(squares)

# now using list comprehension with a codition that only even numbers should be printed
num_squares=[j**2 for j in range(0,11,1) if j%2==0]
print(num_squares)
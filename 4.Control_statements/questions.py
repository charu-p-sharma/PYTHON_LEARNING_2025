"""
Display even numbers from 1 to 10
"""
for i in range(2,11,2):
    print(i)

"""
Display even and odd numbers from 1 to 10
"""
for j in range(1,11):
    if j%2==0:
        print(f"{j} = Is Even number")
    else:
        print(f"{j} = Is Odd number")


"""
Ask user what by what number they want to skip the range
"""

startNum=int(input("Enter the start number = "))
stopNum=int(input("Enter the stop number  = "))
rangeNum=int(input("Enter the range by which u want to skip = "))
if startNum<stopNum:
    if rangeNum <=stopNum and rangeNum>=startNum:
        for i in range(startNum,stopNum,rangeNum):
            print(i)
    else:
        print("The range number is out the range of start and stop number !!")
else:
    print("Start number is less than the stop number !!")


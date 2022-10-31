#Program to Check if a Number is Positive, Negative or 0
num = int(input("Enter the number : "))

if num > 0:
    print("The number", num," is a positive number")
elif num == 0:
    print("The number", num," is a zero number")
else:
    print("The number", num," is a negative number")
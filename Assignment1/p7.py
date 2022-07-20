#Program to Swap Two Variables
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

print("Valuse before swapping are : ",a," and ",b)

temp = a
a = b
b = temp

print("Valuse after swapping are : ",a," and ",b)
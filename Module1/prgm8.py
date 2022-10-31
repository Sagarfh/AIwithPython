#input
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

#floor
floor = a//b
print("The floor of values is ",floor)

#power
power = a ** b
print("The power of values is ",power)

#module
module = a % b
print("The module of values is ",module)
if((a%b)==0):
    print("The module of value is Even")
else:
    print("The module of value is Odd")

#Program to Reverse a Number
num = int(input("Enter the number : "))
num1 = 0

while num != 0:
    digit = num % 10
    num1 = num1 * 10 + digit
    num //= 10

print("Reversed Number is : " + str(num1))
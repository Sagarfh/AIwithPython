#Program to Find Numbers Divisible by Another Number
num1 = int(input("Enter First  Number : "))
num2 = int(input("Enter Second Number : "))
# checking divisibilty.
if num1%num2==0:
    print("\n" +str(num1)+ " is divisible by " +str(num2))
else:
    print("\n" +str(num1)+ " is not divisible by " +str(num2))
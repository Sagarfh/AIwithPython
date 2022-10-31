#Program to Find the Largest Among Three Numbers
a = int(input("Enter the 1st value : "))
b = int(input("Enter the 2nd value : "))
c = int(input("Enter the 3rd value : "))

if(a>b and a>c):
    print(a," is largest of the three numbers")
elif(b>c):
    print(b," is largest of the three numbers")
else:
    print(c," is largest of the three numbers")
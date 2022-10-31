#Program to Check If a String Is a Number (Float)
string = input("Enter the string : ")

# printing original string 
print("The original string : " + str(string))

try : 
    float(string)
    res = True
except :
    res = False

#
print("Is the string entered a number ? : " + str(res))
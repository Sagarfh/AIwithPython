#Calculate the multiplaction and sum of two numbers

def addition(a,b):
    sum = a + b
    print("The answer for addition is ",sum)
    
def subtraction(a,b):
    sub = a - b
    print("The answer for subtraction is ",sub)

def multiplaction(a,b):
    multiplaction = a * b
    print("The answer for multiplaction is ",multiplaction)

def division(a,b):
    div = a / b
    print("The answer for division is ",div)

a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2st number :"))

addition(a,b)
subtraction(a,b)
multiplaction(a,b)
division(a,b)
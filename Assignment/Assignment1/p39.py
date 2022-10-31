#Program to Count the Number of Digits Present In a Number 
num = int(input("Enter a number : \n"))
count = 0

#counting number of digits in 'num'
while num>0:
    count +=1
    num = num//10;
    
print("Number of Digits: ",count)
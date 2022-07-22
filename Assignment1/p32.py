#program to print odd numbers in a List 
list1 = [1,2,3,4,5,6,7,8,9]

print("The given list is : ",list1)
print("The odd numbers are : ")
for num in list1:
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")
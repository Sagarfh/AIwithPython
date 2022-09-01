#Program to find sum of array
array = [1, 2, 3, 4, 5]
sum = 0   

#Loop through the array to calculate sum of elements    
for i in range(0, len(array)):    
    sum = sum + array[i]  
print("The elements in array are : ",array)
print("Sum of all the elements of an array: " + str(sum))
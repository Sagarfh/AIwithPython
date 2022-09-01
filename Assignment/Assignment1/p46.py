#Create a list of tuples from given list having number and its cube in each tuple
List = [6, 2, 5 ,1, 4]

# Creating list of tuples 
tupleList = [(val, (val*val*val)) for val in List]

# print the result
print("The list of Tuples is : " , str(tupleList))
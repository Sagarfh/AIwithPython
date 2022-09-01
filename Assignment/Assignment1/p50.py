#Program to Calculate the Average of Numbers in a Given List
def Average(l): 
    avg = sum(l) / len(l) 
    return avg

list = [1,2,3,4,5,6,7,8,9] 
average = Average(list) 

print("Average of the given list is : ", average)
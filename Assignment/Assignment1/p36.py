#Program to Convert Two Lists Into a Dictionary
list1 = ["Monday", "Tueday", "Wednesday"]
list2 = ["Hi","Hello","Python"]
# Given lists
print("List of K : ", list1)
print("list of V : ", list2)
# COnvert to dictionary
res = {list1[i]: list2[i] for i in range(len(list1))}
print("Dictionary from lists :\n ",res)
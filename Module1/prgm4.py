#Creating a list and printing certian element
list1 = ["Hi","Hello",["Python","Python1","Python2"]]
list2 = ["Sagar",10]

list3 = list1 + list2
print(list3)

print(list3[1])

list4 = list3 + list1

print(list4)
print(list4[2][1])

list5 = ["Python","Python1","Python2",list1]
print(list5)
print(list5[3][2][1])

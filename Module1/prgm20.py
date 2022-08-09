# list functionalities

list1=['alpha','beta','gama','delta']
list2=['d','c','b','a']

#print(cmp(list1,list2))

list3=[1,2,3,4]
print(min(list3))
print(max(list3))

print("Tuple = ",tuple(list1))
print("Set = ",set(list1))

zipped = zip(list1,list2)
print("Zip = ",dict(zipped))

mapped = zipped
print()


list1.append("Ijas")
print(list1)


print(list1+list2)
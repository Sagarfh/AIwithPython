#Dictionaries
Dict = {}
print("Empty Dictionaries:\n")
print(Dict)

#Creating Dictionaries with integer key
Dict = {1:'Geeks',2:'For',3:'Geeks'}
print("Dictionaries with the use of integer key:\n")
print(Dict)
print(Dict[1])

#Creating Dictionaries with mixed key
Dict = {'Name':'Geeks',1:[1,2,3,4]}
print("Dictionaries with the use of mixed key:\n")
print(Dict)
print(Dict['Name'])

#replace value
Dict["Name"] = "Sagar"
print(Dict)
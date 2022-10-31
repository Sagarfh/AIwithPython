#Creating Tuple with the use of String
Tuple1 = ('Python','For')
print("Tuple with the use of String:\n")
print(Tuple1)

#Creating Tuple with nested tuples
Tuple1 = (0,1,2,3)
Tuple2 = ('python','programming','world')
Tuple3 = (Tuple1,Tuple2)
print("Tuple with nested tuples:\n")
print(Tuple3)
print(Tuple3[0][1])

#concatinate
Tuple4 = Tuple1 + Tuple2
print(Tuple4)

Tuple5 = Tuple1 + Tuple2 + Tuple3 + Tuple4
print(Tuple5)
print(Tuple5[4][4])
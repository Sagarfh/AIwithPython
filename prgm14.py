#identity operator
a=10
b=20
c=a

print(a," is not equal to ",b," : ",a is not b)
print(a," is equal to ",c," : ",a is c)
print(id(a))
print(id(b))

a='Hi'
b='Python'
print(id(a))
print(id(b))
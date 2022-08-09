# Functions are bundeled set of instructions that can be repeatedly used again and again.

# Types
# 1.Built-in
# 2.Recursion
# 3.Lambda
# 4.User-defined

#  Function can return data as a result.

String1 = "Hello world"
print("Length of ",String1,"is",len(String1))

pi=3.14
text = 'The value of pi is '+ str(pi)
print(text)


# zip-function
name = ["Sagar","Hemanth","Yusuf","Pushpa"]
roll_no = [4,1,3,2]
#using zip() to map values
mapped = zip(name,roll_no)
print(set(mapped))


# Python prgm to illustrate
# enumerate function
L1 = ["eat","sleep","repeat"]
S1 = "Python"
# creating enumerate objects
obj1=enumerate(L1)
obj2=enumerate(S1)

print("Return type : ",type(obj1))
print(list(enumerate(L1)))
#changing start index to 2 from 0
print(list(enumerate(S1,2)))
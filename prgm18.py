# Control Flows

# Three types of control flow
# 1.Sequential - default mode
# 2. Selection - used for decision and branching
# 3.Repetition - used for looping i.e repeting a piece of code multiple times


# simple if
n = 10
if n % 2 == 0:
    print(n," is an even number ")


# if else
n = 5
if n % 2 == 0:
    print(n," is an even number ")
else:
    print(n," is an odd number ")


# Shorthand if-else
i = 10
print(True) if i < 15 else print(False)


# Nested if
a=5;b=10;c=15
if a>b and a>c:
    print("a = ",a," value is big")
    
elif b>c:
    print("b = ",b," value is big")
else:
    print("last c = ",c," value is big")

# if-elif-else
x=15
y=12
if x==y:
    print(" Both ",x," and ",y," are equal")
elif x>y:
    print(x," is grater than ",y)
else:
    print(x," is smaller than ",y)

# for loop
list = [1,2,3,4,5]

for i in range(len(list)):
    print(list[i], end = " ")
print("\n")

for j in range(0,10):
    print(j, end = " ")
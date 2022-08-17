stack = []

def empty():
    print("Empty Stack")

def push_data(n):
    stack.append(n)

def pop_data():
    if len(stack)==0:
        print("No elements to Delete")
    else:
        stack.pop()

def display():
    if len(stack)==0:
        print("No elements to Display")
    else:
        print(stack)

while True:
    print("1.Push\t 2.Pop\t 3.Display\t 4.Exit")
    n = int(input("Enter the choice : "))

    if n==1:
        element=int(input("Enter the element : "))
        push_data(element)

    elif n==2:
        pop_data()

    elif n==3:
        display()

    elif n==4:
        break

## use of infinet loop as we want our calculator to work forever
## Break the loop as we use infite loop and it has to stopped somewhere
while True:
    option = input("Enter 'Add', 'Subtract', 'Multiply', 'Divide', 'Power' or 'Quit'")
    if option=='Quit':
        break
    elif option=='Add':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x+y)
    elif option=='Subtract':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x-y)
    elif option=='Multiply':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x*y)
    elif option=='Divide':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x/y)
    elif option=='Power':
        x=int(input("Enter the Base: "))
        y=int(input("Enter the exponent: "))
        print(x**y)
    else:
        print("Invalid Argument")
print("Calculator OFF") 

## use of infinet loop as we want our calculator to work forever
## Break the loop as we use infite loop and it has to stopped somewhere
while True:
    option = input("Enter 'add', 'subtract', 'multiply', 'divide', 'power' or 'quit'")
    if option=='quit':
        break
    elif option=='add':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x+y)
    elif option=='subtract':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x-y)
    elif option=='multiply':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x*y)
    elif option=='divide':
        x=int(input("Enter Number 1: "))
        y=int(input("Enter Number 2: "))
        print(x/y)
    elif option=='power':
        x=int(input("Enter the Base: "))
        y=int(input("Enter the exponent: "))
        print(x**y)
    else:
        print("Invalid Argument")
print("Calculator OFF") 

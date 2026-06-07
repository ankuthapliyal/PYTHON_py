while True:

    x = float(input("Enter the first number:- "))
    y = float(input("Enter the second number:- "))

    op = input("Enter input (+, -, *, /, %): ")
                          
    if(op == "+"):
        print("Result: ", x + y)

    elif(op == "-"):
        print("Result: ", x - y)

    elif(op == "*"):
        print("Result: ", x * y)

    elif(op == "/"):
        if (y != 0):
            print("Result =", x / y)
        else:
            print("Division by zero is not allowed")
    
    elif(op == "%"):
        print("Result: ", x % y)

    else:
        print("Invalid opetation")
    
    choice = input("Do you want to continue? (yes/no): ")

    if(choice.lower() != "yes"):
        break

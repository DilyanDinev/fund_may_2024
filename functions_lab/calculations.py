def calculations(operation, n1, n2):
    if operation == "multiply":
        return n1 * n2
    elif operation == "divide":
        return n1 // n2
    elif operation == "add":
        return n1 + n2
    elif operation == "subtract":
        return n1 - n2
    else:
        return "Error incorrect operation"


print(calculations(operation=input(), n1=int(input()), n2=int(input())))

import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2



def calculator():
    global first_number
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    operation = input("Enter the operation (+, -, *, /)")
    second_number = int(input("Enter the second number: "))
    result = operations[operation](first_number, second_number)
    print(result)
    continue_calculating = input("Do you want to continue? (y/n): ")
    if continue_calculating == "y":
        first_number = result
        calculator()


first_number = int(input("Enter the first number: "))
calculator()

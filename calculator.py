"""A simple calculator module that provides basic arithmetic operations."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def floor_divide(a, b):
    """Return the floor division of a by b. Raises ValueError on division by zero."""
    if b == 0:
        return "Cannot divide by zero."
    return a // b


def modulus(a, b):
    """Return the modulus of a by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b


while True:
    # Ask the user for two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    # Ask the user for an operation (+, -, *, /, //, %)
    operation = input("Enter operation ((+, -, *, /, //, %): ")
    # Perform the calculation and display the result
    match operation:
        case "+":
            result = add(num1, num2)
        case "-":
            result = subtract(num1, num2)
        case "*":
            result = multiply(num1, num2)
        case "/":
            result = divide(num1, num2)
        case "//":
            result = floor_divide(num1, num2)
        case "%":
            result = modulus(num1, num2)
        case _:
            result = "Invalid operation"
    print(f"Result: {result}")
    # Allow the user to perform multiple calculations in a loop
    new_operation = input("Do you want to perform another operation? (y/n): ")
    if new_operation == "n":
        print("Exiting the calculator. Goodbye!")
        break

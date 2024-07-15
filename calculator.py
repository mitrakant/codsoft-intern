# Simple Calculator Program

def calculator():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to input an operation choice
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2!= 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation. Please try again.")
        return

    # Display the result
    print("The result is:", result)

# Call the calculator function
calculator()
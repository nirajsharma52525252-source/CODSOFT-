def calculator():
    print("--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("Choose Operation: + , - , * , /")
        operation = input("Enter choice: ")

        if operation == '+':
            print(f"Result: {num1 + num2}")
        elif operation == '-':
            print(f"Result: {num1 - num2}")
        elif operation == '*':
            print(f"Result: {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero.")
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

calculator()
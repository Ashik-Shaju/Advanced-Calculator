print("CALCULATOR")
print("Enter 'C' to Clear / Back, 'CC' To Restart, 'Y' to use the result, 'N' to exit")

def convert_to_string_if_not_float(value):
    try:
        return float(value)
    except ValueError:
        return str(value)

def input_number(prompt):
    while True:
        value = input(prompt).lower()
        if value == 'c':
            return 'c'
        return convert_to_string_if_not_float(value)

def operation():
    while True:
        op = input(f"Enter operation (+, -, *, /, %)  {a}   ").lower()
        if op in ['+', '-', '*', '/', '%', 'c', 'cc']:
            return op

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

def modulus(a, b):
    return a % b

while True:
    current_step = 0  # Track the current input step
    a = None
    op = None
    b = None
    
    while True:
        if current_step == 0:  # Input first number
            a = input_number("Enter 1st Number (or 'c' to clear/back, 'cc' to restart): ")
            if a == 'c':
                continue  # Restart from this step
            elif a == 'cc':
                print("Restarting the calculator...")
                break  # Restart the calculator
            current_step = 1  # Move to the next step
        
        elif current_step == 1:  # Input operation
            op = operation()
            if op == 'c':
                current_step = 0  # Go back to input first number
                continue
            elif op == 'cc':
                print("Restarting the calculator...")
                break  # Restart the calculator
            current_step = 2  # Move to the next step
        
        elif current_step == 2:  # Input second number
            b = input_number(f"Enter 2nd Number (or 'c' to clear/back, 'cc' to restart):  {a} {op} ")
            if b == 'c':
                current_step = 1  # Go back to input operation
                continue
            elif b == 'cc':
                print("Restarting the calculator...")
                break  # Restart the calculator
            
            # Proceed to calculation only if both inputs are valid
            if isinstance(a, float) and isinstance(b, float):
                if op == '+':
                    result = add(a, b)
                elif op == '-':
                    result = subtract(a, b)
                elif op == '*':
                    result = multiply(a, b)
                elif op == '/':
                    result = divide(a, b)
                elif op == '%':
                    result = modulus(a, b)

                print(f"Result:  {a} {op} {b} = {result}")

                # User response handling
                while True:
                    response = input("Enter 'Y' to use result, 'C' to go back to step 2, 'CC' to restart or 'N' to exit: ").lower()
                    if response == 'y':
                        a = result  # Use the result as the new first number
                        current_step = 1  # Go back to input operation
                        break
                    elif response == 'c':
                        current_step = 2  # Go back to input second number
                        break
                    elif response == 'cc':
                        print("Restarting the calculator...")
                        break  # Restart the calculator
                    elif response == 'n':
                        print("Exiting the calculator.")
                        exit()  # Exit the program
                    else:
                        print("Invalid input. Please enter 'Y', 'C', 'CC' or 'N'.")
                continue  # Restart the main loop after handling user response

            else:
                print("One or both values are not numbers.")
                current_step = 0  # Go back to input first number
            
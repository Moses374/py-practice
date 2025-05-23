def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2  # Fixed subtraction

def prod_numbers(num1, num2):
    return num1 * num2

def div_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Result:", add_numbers(num1, num2))
        elif choice == '2':
            print("Result:", subtract_numbers(num1, num2))
        elif choice == '3':
            print("Result:", prod_numbers(num1, num2))
        elif choice == '4':
            result = div_numbers(num1, num2)
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice.")
    except ValueError as e:
        print("Please enter valid numbers.")
    finally:
        print("Calculation attempt complete.")

calculator()

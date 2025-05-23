def div_nums():
    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))

        result=(num1 / num2)

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print(f"{result}")
    finally:
        print("Goodbye")

div_nums()
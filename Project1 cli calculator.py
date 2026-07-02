def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulo by zero.")
    return a % b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return a ** 0.5
OPERATIONS = {"1": ("Add", add, 2),
              "2": ("Subtract", subtract, 2),
              "3": ("Multiply", multiply, 2),
              "4": ("Divide", divide, 2),
              "5": ("Modulo", modulo, 2),
              "6": ("Power", power, 2),
              "7": ("Square Root", square_root, 1),}
def get_number(prompt):
    """Keep asking until the user gives a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def print_menu():
    print("\n" + "=" * 30)
    print("        CLI CALCULATOR")
    print("=" * 30)
    for key, (name, _, _) in OPERATIONS.items():
        print(f"{key}. {name}")
    print("0. Exit")
    print("=" * 30)
def main():
    print("Welcome to the CLI Calculator!")
    while True:
        print_menu()
        choice = input("Choose an operation: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice not in OPERATIONS:
            print("Invalid choice. Please select a valid option.")
            continue
        name, func, arg_count = OPERATIONS[choice]
        try:
            if arg_count == 2:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = func(a, b)
            else:
                a = get_number("Enter number: ")
                result = func(a)
            print(f"\nResult ({name}): {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
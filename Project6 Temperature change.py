def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))
def describe_temperature(celsius):
    """Give a simple human description based on Celsius value."""
    if celsius <= 0:
        return "Freezing"
    elif celsius <= 15:
        return "Cold"
    elif celsius <= 25:
        return "Mild"
    elif celsius <= 35:
        return "Warm"
    else:
        return "Hot"
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
def print_menu():
    print("\n" + "=" * 35)
    print("       TEMPERATURE CONVERTER")
    print("=" * 35)
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit")
    print("=" * 35)
def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            c = get_float("Enter temperature in Celsius: ")
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
            print(f"Condition: {describe_temperature(c)}")
        elif choice == "2":
            c = get_float("Enter temperature in Celsius: ")
            print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
            print(f"Condition: {describe_temperature(c)}")
        elif choice == "3":
            f = get_float("Enter temperature in Fahrenheit: ")
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F = {c:.2f}°C")
            print(f"Condition: {describe_temperature(c)}")
        elif choice == "4":
            f = get_float("Enter temperature in Fahrenheit: ")
            print(f"{f}°F = {fahrenheit_to_kelvin(f):.2f}K")
            print(f"Condition: {describe_temperature(fahrenheit_to_celsius(f))}")
        elif choice == "5":
            k = get_float("Enter temperature in Kelvin: ")
            if k < 0:
                print("Error: Kelvin cannot be negative (below absolute zero).")
                continue
            c = kelvin_to_celsius(k)
            print(f"{k}K = {c:.2f}°C")
            print(f"Condition: {describe_temperature(c)}")
        elif choice == "6":
            k = get_float("Enter temperature in Kelvin: ")
            if k < 0:
                print("Error: Kelvin cannot be negative (below absolute zero).")
                continue
            print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}°F")
            print(f"Condition: {describe_temperature(kelvin_to_celsius(k))}")
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
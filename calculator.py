def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Welcome to the Python Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please choose a valid option.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")

        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

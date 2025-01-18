def calculator():
    print("\nWelcome to the Recursive Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    # Get user input
    choice = input("Enter the number of the operation you want to perform (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        return  # Exit the function to stop recursion

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is {result}")
                else:
                    print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid input! Please choose a valid operation.")

    # Recursively call the function for another operation
    calculator()

# Run the calculator
calculator()

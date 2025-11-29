while True:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Division")
    choice = int(input("Enter the operation (1-4): "))

    if choice == 1:
        print("Result =", x + y)
    elif choice == 2:
        print("Result =", x - y)
    elif choice == 3:
        print("Result =", x * y)
    elif choice == 4:
        if y != 0:
            print("Result =", x / y)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid choice!")

    # Repeat option
    again = input("\nDo you want to calculate again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break

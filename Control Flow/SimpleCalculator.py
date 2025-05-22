def cal():
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        ch = int(input("Enter your choice: "))
        
        match ch:
            case 1:
                a, b = map(int, input("Enter two numbers: ").split())
                print("Result:", a + b)
            case 2:
                a, b = map(int, input("Enter two numbers: ").split())
                print("Result:", a - b)
            case 3:
                a, b = map(int, input("Enter two numbers: ").split())
                print("Result:", a * b)
            case 4:
                a, b = map(int, input("Enter two numbers: ").split())
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Division by zero is not allowed.")
            case 5:
                print("Exiting the calculator.")
                break
            case _:
                print("Invalid choice. Please try again.")

cal()

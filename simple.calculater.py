def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select operation: +, -, *, / (or type 'exit' to quit)")
        
        operation = input("Enter operation: ")
        if operation.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation! Try again.")
            continue

        numbers = input("Enter numbers separated by space: ").split()

        try:
            numbers = [float(num) for num in numbers]
            if not numbers:
                print("No numbers entered!")
                continue

            result = numbers[0]
            for num in numbers[1:]:
                if operation == '+':
                    result += num
                elif operation == '-':
                    result -= num
                elif operation == '*':
                    result *= num
                elif operation == '/':
                    if num == 0:
                        print("Error! Division by zero.")
                        break
                    result /= num

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()
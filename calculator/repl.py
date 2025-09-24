from calculator import operations

def run():
    print("Welcome to CLI Calculator! Type 'exit' to quit.")

    while True:
        try:
            op = input("Enter operation (+, -, *, /): ").strip()
            if op.lower() == "exit":
                print("Goodbye!")
                break

            if op not in {"+", "-", "*", "/"}:
                print("Invalid operation. Please choose +, -, *, /.")
                continue

            a_str = input("Enter first number: ").strip()
            b_str = input("Enter second number: ").strip()

            try:
                a = float(a_str)
                b = float(b_str)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if op == "+":
                result = operations.add(a, b)
            elif op == "-":
                result = operations.subtract(a, b)
            elif op == "*":
                result = operations.multiply(a, b)
            else:  # "/"
                try:
                    result = operations.divide(a, b)
                except ZeroDivisionError as e:
                    print(e)
                    continue

            print(f"Result: {result}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
if __name__ == "__main__":
    run()

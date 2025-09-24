from calculator import operations

OPS = {
    "+": operations.add,
    "-": operations.subtract,
    "*": operations.multiply,
    "/": operations.divide
}

def _handle_operation(op, a, b):
    """Handles arithmetic operations and exceptions."""
    try:
        return OPS[op](a, b)
    except ZeroDivisionError as e:
        return str(e)

def run():
    print("Welcome to CLI Calculator! Type 'exit' to quit.")

    while True:
        try:
            op = input("Enter operation (+, -, *, /): ").strip()
            if op.lower() == "exit":
                print("Goodbye!")
                break

            if op not in OPS:
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

            result = _handle_operation(op, a, b)
            print(f"Result: {result}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run()  # pragma: no cover
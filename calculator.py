def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first_number / second_number
    raise ValueError("Invalid operator. Use +, -, * or /.")


def main():
    print("Calculator (type 'q' to quit)")
    while True:
        raw = input("Enter: number operator number (e.g., 2 + 3): ").strip()
        if raw.lower() == "q":
            break

        parts = raw.split()
        if len(parts) != 3:
            print("Invalid format. Try again.")
            continue

        left, operator, right = parts
        try:
            result = calculate(float(left), operator, float(right))
            if isinstance(result, float) and result.is_integer():
                print(int(result))
            else:
                print(result)
        except (ValueError, ZeroDivisionError) as error:
            print(error)


if __name__ == "__main__":
    main()

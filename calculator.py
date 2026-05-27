def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Division med nul er ikke tilladt.")
        return first_number / second_number
    raise ValueError("Ugyldig operator. Brug +, -, * eller /.")


def main():
    print("Regnemaskine (skriv 'q' for at afslutte)")
    while True:
        raw = input("Indtast: tal operator tal (fx 2 + 3): ").strip()
        if raw.lower() == "q":
            break

        parts = raw.split()
        if len(parts) != 3:
            print("Ugyldigt format. Prøv igen.")
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

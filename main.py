try:
    first_number = float(input("Write first number: "))
    second_number = float(input("Write second number: "))
    operation = input("Write sign operation(+, -, *, /): ")

    result = 0

    if sign == "+":
        result = first_number + second_number
    elif sign == "-":
        result = first_number - second_number
    elif sign == "*":
        result = first_number * second_number
    elif sign == "/":
        if second_number == 0:
            print("You can't divide by zero")
            exit()
        else:
            result = first_number / second_number
    else:
        print("operation not recognize")
    print(f"Result = {result:.2f}")
except ValueError:
    print("Please enter valid numbers")

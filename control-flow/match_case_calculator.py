num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):").lower()

match operation:
    case "+":
        print(f"the result is {num1 + num2}")
    case "-":
        print(f"the result is {num1 - num2}")
    case "*":
        print(f"the result is {num1 * num2}")
    case "/":
        print(f"the result is {num1 / num2}")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case addition:
        sum = num1 + num2
        print(sum)
    case subtraction

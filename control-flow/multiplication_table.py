number = int(input("Enter a number to see its multiplication table:"))

for x in range(1, 11):
    product = x * number
    print(f"{number} * {x}= {product}")

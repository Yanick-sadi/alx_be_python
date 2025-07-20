number = int(input("Enter a number to see its multiplication table:"))

for x in range(1, 10):
    product = x * number
    print(f"{x} * {number} = {product}")

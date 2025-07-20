secret = 7
guess_count = 0
guess = ""
while guess != secret:
    guess_count += 1
    guess = int(input("input it: "))

print("correct")

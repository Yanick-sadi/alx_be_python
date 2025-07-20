import random


secret_number = random.randint(1, 10)

user_guess = int(input("guess the number btn 1 and 10: "))


if user_guess > secret_number:
        print(" higher than mine")
elif user_guess < secret_number:
         print("lower than mine")
elif user_guess == secret_number:
         print("well done")



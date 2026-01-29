import random

num = random.randint(1, 50)
print("I'm thinking of a number between 1 and 50...")
print("You have 3 attempts!\n")

for i in range(1, 4):
    user = int(input(f"Attempt {i}: "))

    if user == num:
        print(f"Correct! You won in {i} attempts! ")
        break
    elif user < num:
        print("Too low!")
    elif user > num:
        print("Too high!")

import random

count = 0
number = random.randint(1, 10)
Name = str(input("Enter your name: "))

print("okay!," , Name, "I am Guessing a number between 1 and 10: ")




while count < 5:
    guess = int(input())
    count += 1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your number is too high")
    elif abs(guess - number) == 1:
        print("You are close")
    elif guess == number:
        print("You guessed it!!!!")
        break
    else:
        print("Please enter a valid number!")
if guess == number:
    print("You guessed it in," + str(count)+ "tries")
else:
    print("You did not guess the number, The number was", + str(number))
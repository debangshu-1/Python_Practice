# Number Guessing Game

import random

randomNum = random.randint(1,100)

counter = 0

print("The range is between 1 to 100 and you get 7 attempts !")
while(counter < 7):

    n = int(input("Enter your guess : "))

    if n == randomNum:
        print("JACKPOT!!!! You guessed right !")
        break
    elif randomNum > n:
        counter = counter + 1
        print(f"Sorry !!! Wrong guess ! {7 - counter} attempts remaining!")
        print("Your guess is smaller . Increase your number .")
    else:
        counter = counter + 1
        print(f"Sorry !!! Wrong guess ! {7 - counter} attempts remaining!")
        print("Your guess is larger . Decrease your number .")

if counter == 7:
    print(f"The number was {randomNum}")
    print("Better Luck Next Time!!!")
import random

number = random.randint(1,10)
guess = int(input("Enter your guessed number from 1 to 10 : "))
close = guess +- 1

while str(number) != guess:
    if guess > 10:
        print("you can't put number above 10")
        exit()
    if guess <= 0:
        print("you can't put number 0 or below !")
        exit()

    if guess == close:
        print("you are close !")

    print("your bad, it was : " + str(number))
    number = random.randint(1, 10)
    guess = int(input("Enter your guess : "))
else:
    print("gg, you found it !")

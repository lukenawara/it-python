import random

print("==================")
print("  GUESS MY NUMBER ")
print("   By Luke        ")
print("==================")
print("")
name = input("what is your name? ")
print("")

guess = -1

print("I'm thinking of a number between 0 and 100. can you guess it?")
the_number = random.randint(1,99)


while guess != the_number:
    guess_text = input ("what is your guess?")
    guess = int(guess_text)
    if guess < the_number:
        print(f"sorry {name}, but your guess is too LOW. Try again.")
    elif guess > the_number:
        print(f"sorry {name}, but your guess is too HIGH. Try again.")
    else:
        print(f"You guessed it! Congratulations, {name}!")

print("Thanks for playing!")
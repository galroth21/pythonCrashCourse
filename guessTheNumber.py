import random

print("Hello. What is your name?")
name = input()    

while True:
    print("\n" + name + ", I'm thinking of a number between 1 and 100.\n")
    secretNumber = random.randint(1,100)
    guess = 0
    tries = 0
    
    # Ask the player to guess 6 times
    while guess != secretNumber:
        print("Take a guess (enter 'quit' to exit):")
        guess = input()
        tries = tries + 1

        if guess == "quit":
            quit()
        elif int(guess) < secretNumber:
            print("Your guess is too low.")
        elif int(guess) > secretNumber:
            print("Your guess is too high.")
        else:
            break       # This condition is the correct guess!

    print("Good job! You guessed my number in " + str(tries) + " guesses!\n\n")
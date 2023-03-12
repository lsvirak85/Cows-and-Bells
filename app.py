import random


def play_game():
    def cows_and_bulls():
        # randomly generate a 4-digit number
        number = str(random.randint(1000, 9999))
        print("Let's play the Cows and Bulls game!")
        print("Guess a 4-digit number.")

        # set the maximum number of guesses
        max_guesses = 5
        num_guesses = 0

        # start the game loop
        while num_guesses < max_guesses:
            # ask the user for a guess
            guess = input("Enter your guess: ")
            num_guesses += 1

            # check if the guess is correct
            if guess == number:
                print("Congratulations! You guessed the number in", num_guesses, "guesses.")
                return

            # check for cows and bulls
            cows = 0
            bulls = 0
            for i in range(4):
                if guess[i] == number[i]:
                    cows += 1
                elif guess[i] in number:
                    bulls += 1

            # print the number of cows and bulls
            print(cows, "cows,", bulls, "bulls")

        # if the user has run out of guesses, display the answer
        print("Sorry, you have run out of guesses. The answer was", number)

    cows_and_bulls()


play_game()

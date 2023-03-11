import random

# generate a random 4-digit number
def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

def count_cows_and_bulls(secret_number, guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if secret_number[i] == guess[i]:
            cows += 1
        elif guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def play_game():
    secret_number = generate_number()
    num_guesses = 0
    while True:
        num_guesses += 1
        guess = input("Enter a 4-digit number: ")
        guess = [int(d) for d in guess]
        cows, bulls = count_cows_and_bulls(secret_number, guess)
        print("Cows:", cows, "Bulls:", bulls)
        if cows == 4:
            print("Congratulations! You guessed the number in", num_guesses, "guesses.")
            break

if __name__ == '__main__':
    play_game()

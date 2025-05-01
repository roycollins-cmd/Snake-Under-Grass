"""
a deductive logic game, you must guess a secret three-digit number based on clues

"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Welcome to Snake Under Grass Bagles. By Al
    
    The computer has a {}-digit secret number with no repetition.
    Try to guess the secret number!
    
    when it says:       that means:
    Pico                One digit is correct but in the wrong position
    Fermi               One digit is correct and in the right position
    Bagels              No digit is correct 
    '''.format(NUM_DIGITS))

    # main game loop.
    while True:
        secret_number = getSecretNum()
        print("I have thought of a number")
        print("you have {} guesses to get.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess#{}".format(numGuesses))
                guess = input('> ')

                clues = getClues(guess,secret_number)
                print(clues)
                numGuesses += 1

                if guess == secret_number:
                    break
                if numGuesses > MAX_GUESSES:
                    print('you ran out of guesses')
                    print('the answer was {}.'.format(secret_number))

            print('do you wanna play again? (yes/no)')
            if not input('> ').lower().startswith('y'):
                break
        print("Thank you for playing!")

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def getClues(guess,secret_number):
    if guess == secret_number:
        return 'You guessed the secret number!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0:
        return 'bagels'
    else:
        clues.sort()
        return ''.join(clues)

if __name__ == '__main__':
    main()



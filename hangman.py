import random
from words import words
from lives_visual_hangman import *
import string


def get_valid_word(words):
    word = random.choice(words)  # chooses a random word from the list 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # user guessed letter
    lives = 7

    # user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left \nand you have used these letters: ', ' '.join(used_letters))

        # 5current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nLetter already used. Guess another one.')

        else:
            print('\nInvalid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('Excellent! You got the word', word, '!')


if __name__ == '__main__':
    hangman()
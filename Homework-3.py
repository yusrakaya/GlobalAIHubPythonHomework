#noinspection PyUnresolvedReferences
#I used this-PyUnresolvedReferences- because my pycharm was not allowed import random and I could not fixed import optimized problem.
import random
word_list = [
    'baby',
    'shark',
    'black',
    'pink',
    'silence',
    'family',
    'turkey',
    'global',
    'community',
    'serendipity',
    'believer',
    'life',
    'beauty',
    'psycho',
    'downfall',
    'blockchain',
    'python',
    'machine',
    'learning',
    'training',
    'love',
    'sunflower'

]
#noinspection PyUnresolvedReferences
#I used this-PyUnresolvedReferences- because my pycharm was not allowed import random and I could not fixed import optimized problem.
from words import word_list

def get_word(word_list):
    # This function returns a random string from the passed list of strings.
    word=random.choice(word_list)
    return word.upper()
def play (word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    name = input("Please enter your name")
    print("Hello", name.capitalize(), "let's start playing Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letter.append(guess)
            else:
                print("Hey man! Good jub,", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed == True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not currect guess man try again.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
            if guessed:
                print("Congratilations, you guessed the word, you win!")
            else:
                print("OMG!, you run out of tries. The word was " + word + "")
def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]








from curses.ascii import isalnum
from wordle import WordleBot

# PATH = "/User/local/bin/chromedriver.exe"

def check_isalnum(word):
    for char in word:
        if not isalnum(char):
            return False

    return True

intro_to_program = """
Hello, welcome to the Wordle Bot Solver!
To begin, enter your preferred starting word that is 5 letters long. 
Then for each guess in Wordle input data in a string where each character represents
if that character was green (g), yellow (y), or grey (r).
"""

print(intro_to_program)

starting_word = input("Select your starting word: ")

while not len(starting_word) == 5 or not check_isalnum(starting_word):
    starting_word = input("The word you entered is not valid, please try again: ")

starting_word = starting_word.lower()

bot = WordleBot("words.txt", starting_word)
bot.solve_wordle()


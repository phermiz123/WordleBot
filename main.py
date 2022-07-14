from curses.ascii import isalnum
from wordle import WordleBot

# PATH = "/User/local/bin/chromedriver.exe"

intro_to_program = """
Hello, welcome to the Wordle Bot Solver!
"""

print(intro_to_program)

bot = WordleBot()
bot.solve_wordle()


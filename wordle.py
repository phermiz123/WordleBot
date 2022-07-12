from typing import Set


def check_data_error(data):
    if not len(data) == 5:
        return True

    for char in data:
        if not char == 'g' or not char == 'y' or not char == 'r':
            return True
    
    return False

class WordleBot:
    def __init__(self, wordsfile, startWord, dataWord_in):

        self.dict = { Set() }
        self.currWord = startWord
        self.dataWord = dataWord_in

        with open(wordsfile, 'r') as file:
            for line in file:
                self.dict[0].append(line)


    def solve_wordle(self):
        guesses = 0

        while guesses < 0:
            guesses += 1
        

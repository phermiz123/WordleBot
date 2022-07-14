import imp
from importlib.resources import path
from typing import Set
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.service import Service
import time

class WordleBot:

    def __init__(self):

        # Setting up all the driver stuff with Selenium
        PATH = "/usr/local/bin/chromedriver.exe"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")

        # Sets up the answers and guess list 
        self.guesses = []
        self.answers = []

        with open("guesses.txt", 'r') as file:
            for line in file:
                self.guesses.append(line)
        
        with open("answers.txt", 'r') as file:
            for line in file:
                self.answers.append(line)
        
        # Clicks out of the pop ups and gets the tiles organized into rows
        time.sleep(5)

        dark = self.driver.find_element(By.CLASS_NAME, "dark")
        dark.click()

        board = self.driver.find_element(By.CLASS_NAME, "Board-module_board__lbzlf")
        self.rows = board.find_elements(By.CLASS_NAME, "Row-module_row__dEHfN")

        


    def get_state_tiles(self, guess_num):
        
        data_state = []
        current_row = self.rows[guess_num].find_elements(By.CLASS_NAME, 'Tile-module_tile__3ayIZ')

        for tiles in current_row:
            tile_state = tiles.get_attribute('data-state')

            if tile_state == 'absent':
                data_state.append(0)
            elif tile_state == 'present':
                data_state.append(1)
            else:
                data_state.append(2)

        return tuple(data_state)


    def solve_wordle(self):

        found_solution = False
        answers = self.answers


        for guesses in range(5):
            
            min_count = 1e6
            guess_word = ""
            best_guess_map = {}
            words_to_consider = []
            
            if guesses == 0:
                words_to_consider = ["arise"]
            else:
                words_to_consider = self.guesses
            
            for word_guesses in words_to_consider:
                
                curr_guess_map = {}

                for possible_answer in answers:
                    colors = self.get_colors(possible_answer, word_guesses)

                    if tuple(colors) not in curr_guess_map:
                        curr_guess_map[tuple(colors)] = [possible_answer]
                    else:
                        curr_guess_map[tuple(colors)].append(possible_answer)


                biggest_answer_list_for_curr_guess = max([len(val) for val in curr_guess_map.values()])


                if biggest_answer_list_for_curr_guess < min_count:
                    min_count = biggest_answer_list_for_curr_guess
                    guess_word = word_guesses

                    best_guess_map = curr_guess_map

            # Enter word and give a slight delay before getting colors from website
            self.enter_word(guess_word)
            time.sleep(5)
            

            data_state = self.get_state_tiles(guesses)

            if data_state in best_guess_map:
                answers = best_guess_map[data_state]
            

            if data_state == [2,2,2,2,2]:
                found_solution = True
                break
            elif len(answers) == 1:
                found_solution = True
                self.enter_word(answers[0])

        if found_solution == True:
            print("Wordle has been solved")
        else:
            print("Could not solve wordle")





    def get_colors(self, answer, guess):

        colors = [0,0,0,0,0]

        # Checks for green
        for i in range(5):
            if guess[i] == answer[i]:
                colors[i] = 2
                answer = answer[:i] + ' ' + answer[i + 1:]
        

        # Checks for yellow
        for i in range(5):
            curr_char = guess[i]
            if curr_char in answer and colors[i] == 0:
                colors[i] = 1
                first_pos = answer.find(curr_char)
                answer = answer[:first_pos] + ' ' + answer[first_pos + 1:]
        
        return tuple(colors)


    def enter_word(self, word):
        dark = self.driver.find_element(By.CLASS_NAME, "dark")
        dark.send_keys(word, Keys.ENTER)

                



        
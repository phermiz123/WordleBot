from doctest import FAIL_FAST
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
    def __init__(self, wordsfile, startWord):
        PATH = "/usr/local/bin/chromedriver.exe"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")
        self.words = []
        self.currWord = startWord

        with open(wordsfile, 'r') as file:
            for line in file:
                self.words.append(line)

        try:
            main_page = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dark"))
            )

            main_page.click()
            main_page.send_keys(startWord, Keys.ENTER)
        except:
            self.driver.quit()

        time.sleep(10)

        board = self.driver.find_element(By.CLASS_NAME, 'Board-module_board__lbzlf')
        self.rows = board.find_elements(By.CLASS_NAME, 'Row-module_row__dEHfN')


    def get_state_tiles(self, guess_num):
        
        data_state = ""
        current_row = self.rows[guess_num].find_elements(By.CLASS_NAME, 'Tile-module_tile__3ayIZ')

        for tiles in current_row:
            tile_state = tiles.get_attribute('data-state')

            if tile_state == 'absent':
                data_state += 'a'
            elif tile_state == 'present':
                data_state += 'p'
            else:
                data_state += 'c'

        return data_state


    def solve_wordle(self):
        guesses = 0
        found_solution = False

        while guesses < 6:

            data_state = self.get_state_tiles(guesses)

            if data_state == "ccccc":
                found_solution = True
                break
            elif len(self.words) == 0:
                break

            self.currWord = self.words[0] 
            
            try:
                main_page = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "dark"))
                )

                main_page.click()
                main_page.send_keys(self.currWord, Keys.ENTER)
            except:
                self.driver.quit()

            time.sleep(10)

            guesses += 1

        if found_solution == True:
            print("Wordle has been solved!")
        else:
            print("Not solved")

        # self.driver.quit()

        
        

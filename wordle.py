import imp
from typing import Set
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class WordleBot:
    def __init__(self, wordsfile, startWord):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")
        self.dict = {}
        self.currWord = startWord

        with open(wordsfile, 'r') as file:
            for line in file:
                self.dict[0] = line

        try:
            main_page = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dark"))
            )
            main_page.click()
            main_page.send_keys(startWord, Keys.ENTER)
        except:
            self.driver.quit()

        self.board = self.driver.find_elements(By.CLASS_NAME, 'Tile-module_tile__3ayIZ')


    def solve_wordle(self):
        guesses = 0
        print(self.board[1].get_attribute('color'))
        self.driver.quit()

        while guesses < 0:
            guesses += 1
        

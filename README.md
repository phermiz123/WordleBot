Hello, welcome to the Wordle Bot. Wordle is a game published by the New York Times. The essence of the game is that you have
six guesses in order to guess the correct five letter word. Once you have guessed the correct word, you have won the game. This bot was inspired by 3Blue1Brown's video on Youtube.

Rules of Wordle: In Wordle, you have six guesses to guess the correct word. For each guess, if that letter does not exist in the correct word it will be grey. If that letter is in the word but is not in the correct position then that letter will be yellow. Finally, if that letter is in the right position and is the correct letter than that letter will be green. You know you have guessed the correct word when all letters turn green.

You can test out a game of Wordle for a better understanding: https://www.nytimes.com/games/wordle/index.html



So, how does the Wordle Bot Work?

The Wordle Bot essentially uses a Greedy-Min-Max algorithm that tries to minimize the largest remaining possible word list. The Bot initially has a loop that loops a maximum of 6 times for each guess. However, we can break out of that early on if we find the correct word before the sixth guess. In this loop there is a double-nested for loop where the outer for loop is all possible guesses that can be made in Wordle and the inner for loop is all possible remaining answers left based on the previous guess. This is essentially O(MN) time complexity where M is the number of guesses and N is on average the number of remaining answers.

What goes on in these for loops?

So, for each possible guess we create a map for that guess and loop through all the possible remaining answers and essentially evaluate what the colors would be for that guess if the possible answer was the answer. Then we add that color as a key to the guesses map and append the possible answer to the value of the key which is a list of the possible remaing answers. Once the answers list is done being looped through, the values of every color is looped through and we find the value that has the largest length. We then compare it to the shortest answer list we have so far and if it is smaller than we make that word the possible guess word and make the map of the current guess word into the best guess word map.

Whats next?

We then enter the chosen guess word onto the actual Wordle website and then get the data on what the actual colors were for our guess. This is all done by using the python library Selenium. If it was all green then we have found the correct answer and can stop our Wordle Bot early. Otherwise, we shorten our answer list by finding the key in that guess word's map and make our possible answer list the value of that key. 

As you can see, our possible answer list will keep getting shorter and shorter until it either becomes a length of one which is our answer or we have run out of guesses. However, I tested this algorithm and it has a 100 percent guess rate based on all possible Wordle answers. Furthermore, it has an average guess rate of 3.77, which is quite solid!

So, if you want to test out this Wordle Bot for yourself then just run this command in the terminal: python3 playWordle.py



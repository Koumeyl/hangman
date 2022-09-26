from curses.ascii import isdigit
import random
import sys

class hangman:

    # possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    possible_words = ['becode']
    max_index = len(possible_words)-1
    word_to_find = list(possible_words[random.randint(0, max_index)])
    temp_correct_word = list(word_to_find)
    lives = 5
    correctly_guessed_letters = ["_"]*len(word_to_find)
    wrongly_guessed_letters = []
    turn_count = 1
    error_count = 0

    
    def play(self):
            print("please enter one letter")
            letter = input()
            if letter.isdigit():
                return print("You did not enter a letter")
            elif len(letter) > 1:
                return print("You cannot enter multple letters or digits")
            elif self.check_guess(letter) == True:
                return print("good guess")
            else:
                return print("bad guess")

    def check_guess(self, letter):
        if(letter in self.temp_correct_word):
            self.correctly_guessed_letters[self.temp_correct_word.index(letter)] = letter
            self.temp_correct_word[self.temp_correct_word.index(letter)] = 0
            return True
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1           
            return False
    
    def game_over(self):
        print("game over...")
        input()
        sys.exit(0)

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
        input()
        sys.exit(0)

    def start_game(self):
        while(self.lives > 0 and "_" in self.correctly_guessed_letters):
            self.play()
            print(f"Well guessed letters: {self.correctly_guessed_letters}")
            print(f"Bad guessed letters: {self.wrongly_guessed_letters}")
            print(f"life: {self.lives}")
            print(f"Error's: {self.error_count}")
            print(f"Turn: {self.turn_count}")
            self.turn_count += 1
            print(f"temp: {self.temp_correct_word}")
            print(f"word to find: {self.word_to_find}")
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

                
            





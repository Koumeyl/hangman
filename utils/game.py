import random

class hangman:

    
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    max_index = len(possible_words)-1
    word_to_find = list(possible_words[random.randint(0, max_index)])
    lives = 5
    correctly_guessed_letters = ["_"]*len(word_to_find)
    wrongly_guessed_letters = []
    turn_count = 0
    error_count = 0
    
    def play(self):
            print("pleas enter a letter")
            letter = input()
            if type(letter) != str:
                return "You did not enter a letter"
            elif len(letter) > 1:
                return "You cannot enter multple letters"
            elif check_gues(letter) == true:
                return "good guess"
            else:
                return"bad guess"

    def check_guess(letter):
        if(letter in word_to_find):
            print()
        return True

                
            





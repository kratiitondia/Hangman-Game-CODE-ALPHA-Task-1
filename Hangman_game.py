#HANGING GAME USING PYTHON
import random

print("Welcome to Hangman Game")
print("-------------------------------------------------------------------------------")

words_list =  ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

random_word = random.choice( words_list)

for x in random_word:
    print("_", end=" ")
def print_hangman_game(incorrect):
    if(incorrect == 0):#1 incorrect 
        print("\n+---+")
        print("|   |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("=======")
        print("Sorry that was incorrect")
    elif(incorrect == 1):  # 2 in correct
        print("\n+---+")
        print("|   |")
        print("O   |")
        print("    |")
        print("    |")
        print("    |")
        print("=======")
        print("Sorry that was incorrect")
    elif(incorrect == 2):
        print("\n+---+")
        print("|   |")
        print("O   |")
        print("|   |")
        print("    |")
        print("    |")
        print("=======")
        print("Sorry that was incorrect")
    elif(incorrect == 3):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("    |")
        print("=======")
    elif(incorrect == 4):
        print("\n+---+")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("    |")
        print("=======")
        print("Sorry that was incorrect")
    elif(incorrect == 5):
        print("\n+---+")
        print(" |   |")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("    |")
        print("=======")
        print("Sorry that was incorrect")
    elif(incorrect == 6):
        print("\n+---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("=========")
        print("Sorry that was incorrect")

def printword(guess_letters):
    counter=0
    right_letters=0
    for char in random_word:
        if(char in guess_letters):
            print(random_word[counter], end=" ")
            right_letters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return right_letters

def printlines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")

length_of_word_to_guess = len(random_word)
No_of_wrong_attempt = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(No_of_wrong_attempt != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
        
    letter_guess = input("\nGuess a letter: ")
    
    if(random_word[current_guess_index] == letter_guess):
        print_hangman_game(No_of_wrong_attempt)
        
        current_guess_index+=1
        current_letters_guessed.append(letter_guess)
        current_letters_right = printword(current_letters_guessed)
        printlines()
        
        
    else:
        No_of_wrong_attempt+=1
        current_letters_guessed.append(letter_guess)

        print_hangman_game(No_of_wrong_attempt)

        current_letters_right = printword(current_letters_guessed)
        printlines()

print(end="\n")

print("Game is over! Thank you for playing...")
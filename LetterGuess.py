#The Hangman Game. - By Anantia Keshri

import random                                                   #importing library

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

complete = False
word_list = ["apple", "banana", "cherry"]                       #list of fruits
chosen_word = random.choice(word_list)                         #using choice function to pick any word at random from the list

#a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

print(f'The chosen word is {chosen_word}.')                    #Used fstring to print it. It is just for testing purpose.

display = []
word_length = len(chosen_word)                                 #stores len of word_list - here it is 2: [0,1,2]
for _ in range(word_length):                                    #for loop to iterate over the word in word_list
    display += "_"                                              #display will increment "_" number of letter in a word from word_list

while not complete:
    guess_word = input("Choose a letter between A to Z:\n").lower()             #takes input from user and converts it in lowercase

    for position in range(word_length):                                         
        letter = chosen_word[position]
        if letter == guess_word:
            display[position] = letter
                
    if guess_word not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    print(f"{' '.join(display)}")
        
    if "_" not in display:
        complete = True
        print("You win.")
        
    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])



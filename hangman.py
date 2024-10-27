#creating a hangman game 
import random
stages=["""
   +---+
   |   |
       |
       |
       |
       |
=========

""","""
    +---+
   |   |
   O   |
       |
       |
       |
=========

""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========

""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========

""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========

""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========

""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========

"""]
word_list=["joshwa","midhun","jaykrishnan"]

lives=0
choosen_word=random.choice(word_list)
print(choosen_word)
display=""*len(choosen_word)
placeholder = ""
word_len = len(choosen_word)

for position in range(word_len):
    placeholder += "_"

print(placeholder)

game_over=False

correct_letters=[]

while not game_over:
    Guess=input("guess a letter:").lower()
    
    new_display=""
    for letter in choosen_word:
        if letter == Guess:
            new_display+=letter
            correct_letters.append(Guess)
        elif letter in correct_letters:
            new_display+=letter
        
        else:
            new_display+="_"
        
    display=new_display
    print(display)

    if Guess not in choosen_word:
        lives+=1
        if lives ==6:
            game_over=True
            print("game over") 

    if "_" not in display :
        game_over=True
        print("you win")
        
    print(stages[lives])


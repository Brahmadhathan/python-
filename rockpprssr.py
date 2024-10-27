#creating a code to play rock paper sissor
import random

rock="""
    _______        
---'   ____)                    
      (_____) 
      (_____)                    
      (____) 
---.__(___)             

"""
paper="""
    _______                    
---'   ____)____           
       _________)_                  
      ____________)              
     ___________)               
---.__________)           
"""
scissors="""
    _______
---'   ____)____
       _________)
       __________)
      (____)
---.__(___)
"""
game_image=[rock,paper,scissors]

user_choice=int(input("what do ypu choose? type 0 for rock, 1 for paper , 2 for scissors  \n"))

print(game_image[user_choice])
computer_choice= random.randint(0,2)
print("computer choice is")
print(game_image[computer_choice])

if user_choice>=3 or user_choice<0 :
    print("enter a valid number you lose")
elif user_choice ==0 and computer_choice==2:
    print("you win!")
elif computer_choice ==0 and user_choice ==2:
    print("you win")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice== user_choice:
    print("its a draw!")





'''
Condation:
    select one of them:
        1. Rock
        2. Paper
        3. Scissor
Case 1:
   Rock - Rock = Tie
   Rock - paper = Paper win
   Rock - Scissor =  Scissor win
     
Case 2:
    Paper - Paper = Tie
    Paper - Rock = Paper win
    Paper - Scissor = Scissor win
    
Case 3: 
    Scissor - Scissor = Tie
    Scissor - Rock = Rock Win
    Scissor - Paper = Scissor Win
''' 

import random

iteam_list = ['Paper','Rock', 'Scissor']
computer_choice = random.choice(iteam_list)
user_choice = input("Enter Your Choice: ").title()

if user_choice == computer_choice:
    print("Match Tie")
    
elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print("Computer Win")
    else:
        print("User Win")
elif user_choice == 'Paper':
    if computer_choice == 'Rock':
        print("User Win")
    else:
        print("Computer Win")
elif user_choice == 'Scissor':
    if computer_choice == 'Rock':
        print('Computer Win')
    else:
        print("User Win")
else:
    print("Invlaid Input plz try again! ")
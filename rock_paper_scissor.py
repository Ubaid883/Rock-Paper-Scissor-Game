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
print(computer_choice)

# while True:
#     print('''
#           Select One of Them
#           1. Rock
#           2. Paper
#           3. Scissor
#           ''')
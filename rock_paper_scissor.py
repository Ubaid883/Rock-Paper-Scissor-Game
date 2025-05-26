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
# select these word by computer
iteam_list = ['Rock', 'Paper','Scissor']
computer_result = 0
user_result = 0
tie_match = 0

# define funcation to proceed Game
def Game(user, computer):
    global user_result, computer_result, tie_match
    if user == computer:
        print("Match Tie")
        tie_match +=1
        print(f'Matches Ties: {tie_match}')
    
    elif user == 'Rock':
        if computer == 'Paper':
            computer_result +=1
            print("Computer Win")
            print(f'Computer Wins Match: {computer_result}')
            
        else:
            print("User Win")
            user_result +=1
            print(f'User Wins Match: {user_result}')
            
    elif user == 'Paper':
        if computer == 'Rock':
            print("User Win")
            user_result +=1
            print(f'User Wins Match: {user_result}')
        else:
            computer_result +=1
            print("Computer Win")
            print(f'Computer Wins Match: {computer_result}')
    elif user == 'Scissor':
        if computer == 'Rock':
            print('Computer Win')
        else:
            print("User Win")
            user_result +=1
            print(f'User Wins Match: {user_result}')
    else:
        print("Invlaid Input plz try again! ")
        
while True:
    print('''
          Write This Ones 
          Rock, Paper, Scissor
          4. Exit
          '''
          )
    computer_choice = random.choice(iteam_list)
    user_choice = input("Enter Your Choice, (Rock, Paper, Scissor): ").title()
    Game(user_choice, computer_choice)
    if user_choice == '4':
        break
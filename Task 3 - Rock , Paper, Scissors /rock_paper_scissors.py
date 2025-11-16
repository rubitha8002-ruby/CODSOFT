# Rock Paper Scissors Game - CofSoft Task 4
import random
while True:
    choices = ['rock', 'paper', 'scissors']

    # User input
    user_choice=input("Enter your choice (rock/paper/scissors):").lower()
    # Checking for invalid input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors")
    # Computer choice
    else:
        computer_choice= random.choice(choices)
        print("Computer chose:",computer_choice)
    # Determining the winner
        if user_choice== computer_choice:
            print("The game is tied!")
        elif (user_choice=='rock' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock'):
            print("You Win!")
        else:
            print("Computer Wins!")

    # Asking for a rematch
    rematch= input("Want to play again? (Yes/No):").lower()
    if rematch!='yes':
        print("Thanks for playing!")
        break
   
                                                                                                                      

import random

#Starts the game
print("\nIt's a Rock Paper Scissors Game.")

#Tuple for computer and user to choose
sequence = ("rock", "paper", "scissors")
options =("y","n")

#Rounds of game
round = 1

#User score in game 
user_score = 0

#Computer score in game
computer_score = 0

enter_game = input("\nWould you like to play Rock Paper Scissors? (y/n): ").lower()

#Checks for user input if it is valid or not
while enter_game not in options :
    enter_game = input ("Please enter a valid answer (y/n): ").lower()

#Looping if user wants to play
while enter_game == "y" :

    #Random choice for computer out of tuple sequence
    computer_choice = random.choice(sequence)

    print("ROUND ",round)
    
    #Asking user for user's choice out of sequence
    user_choice = input("\nChoose your choice (rock/paper/scissors): ").lower()
    
    #Checking if user input is out of tuple sequence or not
    while user_choice not in sequence :
        user_choice = input("Please choose a valid choice (rock/paper/scissors): ").lower()
        

    #Condition when user win against the computer
    if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") :
        
        print("You won!")
        round += 1
        user_score += 1

    #Condition where user and computer have a tie
    elif user_choice == computer_choice :
        
        print("It's a tie.")
        round += 1
    
    #Condition when user lost against computer
    else :
        round += 1
        computer_score += 1
        print ("You lost!")
        

    #Choices and Score display    
    print("Computer: ", computer_choice,"\n","    You: ", user_choice)
    print("\nComputer: ", computer_score,"\n","    You: ", user_score)
          
    enter_game = input("\nDo you like to play again?(y/n)").lower()
    
    #Checks for user input if it is valid or not
    while enter_game not in options :
        enter_game = input ("Please enter a valid answer (y/n): ")

#Condition when user denies to play 
if enter_game == "n" :
    print("\nSee you soon! \nBye. \n")
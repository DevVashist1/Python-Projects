import random

#Starts the game
print("It's a Rock Paper Scissors Game.")

sequence = ("rock", "paper", "scissors")
entry = input("Enter the game(y/n): ")
entry = entry.lower()

while True :
    if entry == "y" :
        
        computer = random.choice(sequence)

        tries = input("Enter your choice (rock, paper or scissors): ")
        tries = tries.lower()

        if computer == "rock" and tries == "paper" :
            print ("You won!")
            print("Computer : ",computer,"\n","You : ",tries)
        elif computer == "rock" and tries == "scissors" :
            print ("You lost!")
            print("Computer : ",computer,"\n","You : ",tries)
        elif computer == "paper" and tries == "rock" :
            print ("You lost!")
            print("Computer : ",computer,"\n","You : ",tries)
        elif computer == "paper" and tries == "scissors" :
            print ("You won!")
            print("Computer : ",computer,"\n","You : ",tries)
        elif computer == "scissors" and tries == "rock" :
            print ("You won!")
            print("Computer : ",computer,"\n","You : ",tries)
        elif computer == "scissors" and tries == "paper" :
            print("You lost!")
            print("Computer : ",computer,"\n","You : ",tries)
        elif computer == tries:
            print("It's a tie.")
            print("Computer : ",computer,"\n","You : ",tries)
        else :
            print("Enter a Valid Input (rock/paper/scissors).\n")
        
        entry = input("Try again?(y/n) : ")
        entry = entry.lower()

    elif entry == "n" :
        print("See you soon! Bye.")
        break
    else :
        print("Enter a Valid Input (y/n).")
        entry = input("Try again?(y/n) : ")
        continue
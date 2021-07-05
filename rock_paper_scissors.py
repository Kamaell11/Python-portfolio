import random

def play():
    options = ["rock", "paper", "scissors"]
    
    score = [0,0] #let's say computer score is score[0] and players is score [1]
    rounds = 0
    while score[0] != 3 and score[1] !=3:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        player_choice = input("Please type: rock, paper, or scissors: ")

        #player has typed wrong choice
        if player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
            print("Something went wrong, type Your choice again")

        #draw
        if player_choice == "rock" and computer_choice == options[0] or player_choice == "paper" and computer_choice == options[1] or player_choice == "scissors" and computer_choice == options[2]:

            rounds += 1
            print(f"Round: {rounds} \n Computer chose: {computer_choice} \n Player chose: {player_choice}  \n It's a draw! \n Computer score: {score[0]} Player score: {score[1]}")

       #player wins
        if player_choice == "paper" and computer_choice == options[0] or player_choice == "scissors" and computer_choice == options[1] or player_choice == "rock" and computer_choice == options[2]:
            score[1] += 1
            rounds += 1
            print(f"Round: {rounds} \n Computer chose: {computer_choice} \n Player chose: {player_choice}  \n Player wins! \n Computer score: {score[0]} Player score: {score[1]}")
       
        #computer wins
        if player_choice == "scissors" and computer_choice == options[0] or player_choice == "paper" and computer_choice == options[2] or player_choice == "rock" and computer_choice == options[1]:
            score[0] += 1
            rounds += 1
            print(f"Round: {rounds} \n Computer chose: {computer_choice} \n Player chose: {player_choice}  \n Computer wins! \n Computer score: {score[0]} Player score: {score[1]}")

        
        if score[0] == 3:
            print("Computer has won the game!")

        elif score[1] == 3:
            print("Player has won the game!")
play()
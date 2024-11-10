#ROCK PAPER SCISSOR GAME BY PRAKASH
#type rock or scissor or paper for input or quit to exit the game
import random

options = ["rock", "paper", "scissors"]


def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper") or \
            (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    while True:
        # Ask player for input
        player = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if player == "quit":
            print("Thanks for playing!")
            break

        if player not in options:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)
        print(result)
        print()


play_game()

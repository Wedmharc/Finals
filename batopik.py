import random

def play_game():
    wins = 0
    losses = 0
    while wins < 2 and losses < 2:
        print("Rock, Paper, Scissors?")
        player = input().capitalize()
        computer = random.choice(["Rock", "Paper", "Scissors"])
        print(f"Computer chose {computer}")
        if player == computer:
            print("Tie!")
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            print("You win this round!")
            wins += 1
        else:
            print("You lose this round!")
            losses += 1
        print(f"Score: You {wins}, Computer {losses}\n")
    if wins == 2:
        print("You win the game!")
    else:
        print("Computer wins the game!")

play_game()
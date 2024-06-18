import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_wins = 0
    computer_wins = 0
    while player_wins < 2 and computer_wins < 2:
        print("Rolling the dice...")
        player_roll = roll_dice()
        computer_roll = roll_dice()
        print(f"Player rolled a {player_roll}")
        print(f"Computer rolled a {computer_roll}")
        if player_roll > computer_roll:
            print("Player wins this round!")
            player_wins += 1
        elif player_roll < computer_roll:
            print("Computer wins this round!")
            computer_wins += 1
        else:
            print("It's a tie!")
        print(f"Score: Player {player_wins}, Computer {computer_wins}\n")
    if player_wins == 2:
        print("Player wins the game!")
    else:
        print("Computer wins the game!")

play_game()
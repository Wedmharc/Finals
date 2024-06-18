def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]!= " ":
            return board[condition[0]]
    if " " not in board:
        return "Tie"
    return False

def play_game():
    player1_name = input("Enter player 1's name: ")
    player2_name = input("Enter player 2's name: ")
    board = [" "] * 9
    current_player = player1_name
    while True:
        print_board(board)
        move = input(f"{current_player}'s turn. Enter a number (1-9): ")
        if board[int(move) - 1]!= " ":
            print("Invalid move, try again.")
            continue
        board[int(move) - 1] = "X" if current_player == player1_name else "O"
        result = check_win(board)
        if result:
            print_board(board)
            if result == "Tie":
                print("It's a tie!")
            else:
                print(f"{result} wins!")
            break
        current_player = player2_name if current_player == player1_name else player1_name

play_game()
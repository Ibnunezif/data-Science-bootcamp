import os

def draw_board(board):
    """Prints the current state of the 3x3 board."""
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal for all window, mac and linux os
    print(" Tic-Tac-Toe ")
    print("-------------")
    for row in range(3):
        print(f"| {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} |")
        print("-------------")

def check_win(board, player):
    # define the winning combination
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in win_combinations:
        # Check if ALL three spots in this combo match the player
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
            
    return False # No winning combination found

def play_game():
    # Initialize board with numbers 1-9 to guide players
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves = 0

    while moves < 9:
        draw_board(board)
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            if board[choice] in ["X", "O"]:
                print("Spot taken! Try again.")
                # Small pause so the user can read the message before the screen clears
                input("Press Enter to continue...")
                continue
            
            # Update board and check for win
            board[choice] = current_player
            moves += 1
            
            if check_win(board, current_player):
                draw_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                return
            
            # Switch player
            current_player = "O" if current_player == "X" else "X"
            
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            input("Press Enter to continue...")

    draw_board(board)
    print("It's a draw!")

def main():
    while True:
        play_game()
        # Ask the user if they want to restart
        restart = input("\nDo you want to play again? (y/n): ").lower()
        if restart != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


## Tic-Tac-Toe (Python CLI)
A simple, interactive Tic-Tac-Toe game built for the terminal using Python. This version supports two players, automatic board clearing for a clean UI, and a "Play Again" feature.
## 🚀 Features

* Cross-Platform: Works on Windows, macOS, and Linux (automatically detects and uses the correct clear-screen command).
* Interactive UI: Displays a 3x3 grid with numbered spots (1-9) to make choosing moves easy.
* Input Validation: Handles invalid inputs (letters or out-of-range numbers) and prevents players from overwriting taken spots.
* Replayability: Includes a game loop that asks if you want to play another round after a win or a draw.

## 🛠️ How to Run

   1. Ensure you have Python installed.
   2. Save the code into a file named tictactoe.py.
   3. Open your terminal or command prompt.
   4. Navigate to the folder containing the file and run:
   
   ``` python tictactoe.py ```
   
   
## 🎮 How to Play

   1. The board is numbered from 1 to 9.
   2. Player X goes first.
   3. Type the number corresponding to the spot where you want to place your mark and press Enter.
   4. The game will automatically check for a winner (3 in a row, column, or diagonal).
   5. If all 9 spots are filled without a winner, the game ends in a draw.

## 📝 Code Logic

* draw_board(): Uses os.system to clear the terminal so the board stays in one place.
* check_win(): Iterates through a list of tuples representing all possible winning combinations.
* play_game(): Manages the individual match logic, turn switching, and move counting.
* main(): Controls the high-level loop that allows for multiple matches.



# get_validated_input.py
import globals

'''
This function is used to safely get the player's chosen cell input (row and column).  
We want to make sure the player does not enter anything that would break the game,  
like letters, too many numbers, or coordinates outside the board.

The function keeps asking the player to type in two numbers separated by a space,  
for example “1 2”. These numbers represent the row and column of the cell they want to pick.  

The main things that are checked when a player inputs a value:
1. The player has to enter exactly two values (row and column).
2. Both values have to be integers (no letters or symbols).
3. The row and column has to be inside the board’s size (not negative or too large).
4. The cell they pick has to still be hidden, so they can’t pick one that’s already revealed.

If any of these checks fail, the player is told what went wrong and asked again.  
Once a valid input is given, the function returns the (row, col) position that can be used in the game.
'''

HIDDEN_SYMBOL = ' ♦ '

def get_validated_input(board):
    """
    Ask the player for a row and column.
    Keep asking until:
    - both are integers
    - inside the board
    - the chosen cell is still hidden
    """
    while True:
        raw = input("Enter row and column (e.g. 1 2): ")
        parts = raw.split()

        # must be exactly two parts
        if len(parts) != 2:
            print("Please enter exactly two numbers.")
            continue

        # both parts must be integers
        try:
            row = int(parts[0])
            col = int(parts[1])
        except ValueError:
            print("Both row and column must be numbers.")
            continue

        # inside board bounds
        if not (0 <= row < globals.ROWS and 0 <= col < globals.COLS):
            print("Out of bounds. Try again.")
            continue

        display, base = board[row][col]

        # must still be hidden
        if display != HIDDEN_SYMBOL:
            print("That cell is already revealed. Pick another.")
            continue

        # valid move
        return row,col

import globals
import random

'''
Now, we need to disperse the amount of selected mines throughout the board randomly, by replacing the hidden layer 
of the tuples where the mines go, with a mine. This entails remaking those tuples competely however. 
Through research, we've found that there are two main ways to randomize: with and without replacement. Since we
don't want to have mines be placed on the same spot, we will need to use without replacement (like pulling numbers
in bingo, once a number has been pulled, it can't be pulled again).

First we'll make the globals easier to work with and ensure that their values fit our criteria.

Then we collect all the coordinate pairs in a list, to then use the random.sample to select mine positions.
Thereafter we change the given cells, by keeping the display but changing the base to a bomb.
'''

def place_random_mines(board):
    rows = globals.ROWS
    cols = globals.COLS
    mines = globals.MINES

    if not isinstance(rows, int) or rows < 2 or rows > 10:
        print("Invalid number of rows. Must be between 2 and 10.")
        return

    if not isinstance(cols, int) or cols < 2 or cols > 10:
        print("Invalid number of columns. Must be between 2 and 10.")
        return

    if not isinstance(mines, int) or mines < 1 or mines >= rows * cols:
        print(f"Invalid number of mines. Must be between 1 and {rows * cols - 1}.")
        return

    #build a list of all coordinates, [(0,0), (0,1), ...]
    all_cells = [(r, c) for r in range(rows) for c in range(cols)] 

    #chooses MINES unique coordinates, this way without replacements
    mine_positions = random.sample(all_cells, mines)

    #for each mine coordinate, rebuild the tuple: (display, '💣')
    for (r, c) in mine_positions:
        display, _ = board[r][c] #keep existing display (' ♦'), but we don't care about the base of the tuple
        board[r][c] = (display, '💣') #replace BASE with bomb

    return board
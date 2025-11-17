import globals

'''
First we want to initialize the board. Things to be aware of here are that we need a 3D board. 
We need the 2D rows and columns that the player sees, but we need to have a level deeper, that indicates number,
bomb or blank. We do this by making a row into a list that's as long as the ROWS input, and this list consists of
tuples/sets that will contain the contents of each layer. Layer 0 will be the displayed level, and layer 1 will 
be the hidden one, containing either a number, a bomb or nothing (blank). This list gets repeated for COLS input
amount of times. 

We want to verify the input for the board for certain characteristics. Rows and cols we wanted at least 2, so the 
game can actually be played, and we didn't want more than a 10*10 board, so we put that as max.

For the MINES, the rules were that we wanted at least 1 mine, so it's not just a win on first move, and the amount
of mines couldn't be more than the product of the ROWS and COLS, as it would make the game unplayable.
'''

def initialize_board():
    # ROWS - for all these variables it's important to adapt the global variables.
    prompt_rows = 'Please define number of rows (min. 2 and max. 10): '
    while True:
        try:
            globals.ROWS = int(input(prompt_rows))
            if globals.ROWS < 2 or globals.ROWS > 10:
                raise ValueError
            break
        except ValueError:
            prompt_rows = 'Invalid. Try again (min. 2 and max. 10): '
    
    # COLS
    prompt_cols = 'Please define number of columns (min. 2 and max. 10): '
    while True:
        try:
            globals.COLS = int(input(prompt_cols))
            if globals.COLS < 2 or globals.COLS > 10:
                raise ValueError
            break
        except ValueError:
            prompt_cols = 'Invalid. Try again (min. 2 and max. 10): '
    
    # MINES
    prompt_mines = f'Please define number of mines (1–{globals.ROWS * globals.COLS - 1}): '
    while True:
        try:
            globals.MINES = int(input(prompt_mines))
            if globals.MINES >= globals.ROWS * globals.COLS or globals.MINES < 1:
                raise ValueError
            break
        except ValueError:
            prompt_mines = f'Invalid. Try again (1–{globals.ROWS * globals.COLS - 1}): '

    # Create empty board
    board = [
        [(' ♦ ', '   ') for _ in range(globals.COLS)] 
        for _ in range(globals.ROWS) #level 0 is the diamond and level 1 is waiting for blank, bomb or number
    ]

    return board #board ready to use for place_random_mines.py

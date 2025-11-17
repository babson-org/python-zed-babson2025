import globals

'''
This function will make it easier to grab the cells that need to be checked. 
First we need deltas to be able to work with each cell around the selected one. 
So if we pick cell (1, 2), the one above, N(orth) or (-1, 0), will have one less row, but be the same column 
ie. using the example above: (1-1, 2+0) -> (0, 2). We will loop through all of these to get all the adjacent cells.

This raises the problem of subtracting e.g. 1 from a 0 coordinate wherein we would end up outside the board.
This problem is adressed through creating a variable for the max rows and cols value, so we can if statement to
keep the coordinates between 0 and the max.
'''

_DELTAS = [
    (-1,  0),  # N
    (-1,  1),  # NE
    ( 0,  1),  # E
    ( 1,  1),  # SE
    ( 1,  0),  # S
    ( 1, -1),  # SW
    ( 0, -1),  # W
    (-1, -1),  # NW
]

def get_adjacent_cells(row, col): 
    #in english, this function is taking row and col input from when it's called and 
    # is returning a list containing coordinate pairs in tuples.
    
    neighbors = [] #the list we'll be appending to that'll be returned

    max_r, max_c = globals.ROWS, globals.COLS
    #we need these variables, as we don't want anything outside of the board. 
    #E.g. the row can't be less than 0 or more than the ROWS input, which we'll make sure of with an if statement.

    for dr, dc in _DELTAS: #dr and dc is the delta in rows and delta in cols, what all the _DELTAS contained.
        nr, nc = row + dr, col + dc #nr and nc is New row and New col
        #this loops us through the Deltas (each surrounding cell), and gives us the cell value IF...
        if 0 <= nr < max_r and 0 <= nc < max_c: #... this is true. Then it'll append it to neighbors.
            neighbors.append((nr, nc))

    return neighbors

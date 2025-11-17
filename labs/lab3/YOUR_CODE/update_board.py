# update_board.py
from get_adjacent_cells import get_adjacent_cells

HIDDEN_SYMBOL = ' ♦ '
BLANK_SYMBOL = '   '   

def update_board(board, start_row, start_col):
    """
    This file is in charge of revealing cells after the player picks a spot.
The board has two “layers” stored together:
- the display layer 
- the base layer 


The flow:
1. Start with the cell the player picked.
2. If it is a number, just flip it over.
3. If it is blank, flip it over and also check all its neighbors.
4. Keep expanding through the blank cells until there are no more left
   to reveal.
    """

    stack = [(start_row, start_col)]

    while stack:
            r, c = stack.pop()

            display, base = board[r][c]

            # if already revealed, skip
            if display != HIDDEN_SYMBOL:
                continue

            # if this cell is a number (and not a mine)
            if base != BLANK_SYMBOL and base != '💣':
                # show the number by copying base into display
                board[r][c] = (base, base)
                continue

            # if this cell is blank
            if base == BLANK_SYMBOL:
                # reveal this blank
                board[r][c] = (BLANK_SYMBOL, base)

                # look at neighbors
                for nr, nc in get_adjacent_cells(r, c):
                    n_display, n_base = board[nr][nc]

                    # only consider hidden, non-mine neighbors
                    if n_display == HIDDEN_SYMBOL and n_base != '💣':
                        if n_base == BLANK_SYMBOL:
                            # blank neighbor: push to stack to expand further
                            stack.append((nr, nc))
                        else:
                            # number neighbor: reveal it, but don't expand from it
                            board[nr][nc] = (n_base, n_base)

    # return AFTER the loop finishes processing all items
    return board
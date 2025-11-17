import globals
from get_adjacent_cells import get_adjacent_cells
from is_mine_at import is_mine_at

_BLANK = '   '

def count_adjacent_mines(board):
    """
    For every NON-mine cell, count the number of adjacent mines and
    write log count into the BASE layer:
      - if count == 0 then the base becomes BLANK ('   ')
      - if count > 0 then the base becomes a 3-wide string like ' 2 '

    Does not touch the display layer or modify mine cells.
    Returns the same board object for convenience.
    """
    rows, cols = globals.ROWS, globals.COLS

    for r in range(rows):
        for c in range(cols):
            if is_mine_at(board, r, c):
                continue  # ignore the mines 

            # count neighboring mines
            count = 0
            for nr, nc in get_adjacent_cells(r, c):
                if is_mine_at(board, nr, nc):
                    count += 1

            # update BASE layer with number or blank
            display, _ = board[r][c]
            if count == 0:
                board[r][c] = (display, _BLANK)
            else:
                board[r][c] = (display, f' {count} ')
    return board
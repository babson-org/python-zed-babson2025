
_DIAMOND = ' ♦ '  # unrevealed marker on the DISPLAY layer

def game_won(board):
    """
    Return True when ALL safe cells have been revealed.
    A cell is "safe" if its BASE is not a mine. We consider the game won
    when there are no unrevealed diamonds over safe cells.
    """
    for row in board:
        for display, base in row:
            if base != '💣' and display == _DIAMOND:
                return False
    return True
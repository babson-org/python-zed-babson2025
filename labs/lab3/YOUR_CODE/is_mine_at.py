# is_mine_at.py
def is_mine_at(board, row, col):
    """
    Return True iff the hidden/base layer at (row, col) is a mine. 
    Essentially accessing the base layer (index 1) of the cell
    """
    return board[row][col][1] == '💣'

from calc_score import calc_score
def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    
    if calc_score(board) != 0:
        return True

    filled = all(abs(cell) == 10 for cell in board)
    return filled


   
    



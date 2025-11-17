# play_minesweeper.py
from initialize_board import initialize_board
from place_random_mines import place_random_mines
from count_adjacent_mines import count_adjacent_mines
from get_validated_input import get_validated_input
from update_board import update_board                        
from is_mine_at import is_mine_at
from game_won import game_won
from print_board import print_board


'''
This file is basically where the whole Minesweeper game comes together.
Each helper function in the other files does one small job, and this file
is the one that controls the “flow” of the game.

The way it works is:
1. We create the empty board.
2. We place random mines.
3. We calculate the numbers around each mine.
4. Then we enter a loop where the player keeps choosing spots until:
    - they hit a mine (lose), or
    - they reveal all safe cells (win)

This file doesn’t deal with the details of how mines are placed or how
blanks spread. It just calls the functions that handle those pieces.
'''

def reveal_all_mines(board):
    """
    Show all mines when the player loses by replacing the display layer with the mine symbol 💣.
    """
    for r in range(len(board)):
        for c in range(len(board[0])):
            display, base = board[r][c]
            if base == '💣':
                board[r][c] = ('💣', base)


def play_minesweeper():
    """
    Main function to run the Minesweeper game.
    Handles setup, input, revealing cells, win/lose checks,
    and printing the board after each move.
    """
    # 1. Setup
    board = initialize_board()
    place_random_mines(board)
    count_adjacent_mines(board)

    # 2. Game loop
    while True:
        print_board(board, 0)
        
          # show visible layer                      

        row, col = get_validated_input(board)    

        # get a valid move  

        # if the player hits a mine
        if is_mine_at(board, row, col):
            reveal_all_mines(board)
            print_board(board, 0)
            print("You hit a mine. Game over!")
            break

        # if cell is safe, reveal cells
        update_board(board, row, col)

        # checks if the player won
        if game_won(board):
            print_board(board, 0)
            print("You cleared all safe cells! You win!")
            break


# Run the game only when this file is executed directly
if __name__ == "__main__":
    play_minesweeper()
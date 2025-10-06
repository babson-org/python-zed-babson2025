    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            move = int(input(prompt))
            #between 1 and 9
            if move < 1 or move > 9:
                raise ValueError
            idx = move -1

            #checks if spot is filled
            if board[idx] == 10 or board[idx] == -10:
                prompt = "Spot is filled. Try again"
                continue
            board[idx] = score['player']
            break

    
            
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
   

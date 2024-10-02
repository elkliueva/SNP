class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):

    if len(players) != 2:
        raise WrongNumberOfPlayersError
    
    moves = ['R', 'P', 'S']
    
    player1_name, player1_move = players[0]
    player2_name, player2_move = players[1]

    if player1_move not in moves or player2_move not in moves:
        raise NoSuchStrategyError

    if player1_move == player2_move:
        return f'{player1_name} {player1_move}'

    if (player1_move == 'R' and player2_move == 'S') or (player1_move == 'S' and player2_move == 'P') or (player1_move == 'P' and player2_move == 'R'):
        return f'{player1_name} {player1_move}'
    
    return f'{player2_name} {player2_move}'

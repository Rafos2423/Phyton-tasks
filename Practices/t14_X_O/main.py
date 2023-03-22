from Practices.t14_X_O.Move import Move
from Practices.t14_X_O.Board import Board

class Game:
    def __init__(self):
        move = Move()
        board = Board()
        icon = 'X'

        while True:
            move.player_move(board, icon)

            if board.is_full():
                print('Board is full')
                break

            if board.is_victory():
                print(f'Player with {icon} win')
                break

            if icon == 'X':
                icon = 'O'
            elif icon == 'O':
                icon = 'X'
        
        print('The game ends')
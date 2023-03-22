from Practices.t14_X_O.Move import Move
from Practices.t14_X_O.Board import Board

move = Move()
board = Board()

icon1 = 'O'
icon2 = 'X'

while True:
    board.print_board()

    while True:
        pos = Move.input_position_move()
        if board.add_to_board(pos, icon):
            break

    if board.is_full():
        print('Board is full')

    if board.is_victory():
        print(f'Player with {icon} win')


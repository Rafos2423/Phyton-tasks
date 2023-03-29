from Practices.t14_X_O.Board import Board
import random
class Move:
    def __input_position_move(self):
        choice = input('\nEnter your move 1-9: ')

        if not choice.isdigit():
            print('Enter a number')
            return Move.__input_position_move(self)

        if int(choice) < 0 or int(choice) > 9:
            print('Number must be 0-9')
            return Move.__input_position_move(self)

        return int(choice) - 1
    def __computer_position_move(self, board):
        for row in board.victory_positions:
            symbols = []
            for i in range(len(row)):
                symbols.append(board[row[i]])
            print(symbols)




    def player_move(self, board, icon):
        board.print_board()

        while True:
            pos = Move.__computer_position_move(self, board)
            if board.add_to_board(pos, icon):
                break





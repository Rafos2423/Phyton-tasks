from TasksOnLessons.X_O.Board import Board

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




    def player_move(self, board, icon):
        board.print_board()

        while True:
            pos = Move.__input_position_move(self)
            if board.add_to_board(pos, icon):
                break





class Board:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.victory_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

    def add_to_board(self, pos, symb):
        if self.board[pos] == ' ':
            self.board[pos] = symb
            return True
        else:
            print('That space is taken')
            return False

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
        row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
        row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])
        delimeter = '+---+---+---+'
        print(f"\n {delimeter} \n {row1} \n {delimeter} \n {row2} \n {delimeter}  \n {row3} \n {delimeter} ")

    def is_victory(self):
        Olist = list(filter(lambda x: x == ['X', ' ', ' '], self.victory_positions))
        return self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' ' or \
                self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' ' or \
                self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' ' or \
                self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ' or \
                self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ' or \
                self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ' or \
                self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' '


    def is_full(self):
        return not self.board.__contains__(' ')
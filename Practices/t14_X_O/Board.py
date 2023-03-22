class Board:
    def __init__(self):
        self = [' ' for i in range(9)]

    def add_to_board(self, pos, symb):
        if self[pos] == ' ':
            self[pos] = symb
            return True
        else:
            print('That space is taken')
            return False

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self[0], self[1], self[2])
        row2 = '| {} | {} | {} |'.format(self[3], self[4], self[5])
        row3 = '| {} | {} | {} |'.format(self[6], self[7], self[8])
        delimeter = '+---+---+---+'
        print(f"\n {delimeter} \n {row1} \n {delimeter} \n {row2} \n {delimeter}  \n {row3} \n {delimeter} ")

    def is_victory(self):
        return self[0] == self[1] == self[2] or \
                self[3] == self[4] == self[5] or \
                self[6] == self[7] == self[8] or \
                self[1] == self[4] == self[7] or \
                self[2] == self[5] == self[8] or \
                self[0] == self[4] == self[8] or \
                self[2] == self[4] == self[6]


    def is_full(self):
        return not self.__contains__(' ')
class InvalidColumnError(Exception):
    '''Error when trying to add a piece to the column thatis already filled.
    '''
    pass


class Board:
    '''Class that defines the connect four board, and holds methods for
    the board class.
    '''
    __RED = '\033[91m'
    __YELLOW = '\033[93m'
    __ENDC = '\033[0m'

    def __init__(self):
        '''Inits with a board with the dimensions of 6 by 7 and fills the
        the board with the placeholder.
        '''
        row, col = 6, 7
        self.__placeholder = '.'
        self.__board = [
            [self.__placeholder for _ in range(col)] for _ in range(row)]
        self.__col_counter = [row - 1 for _ in range(col)]

    def __str__(self):
        '''Turns the board into a a formatted string that displays the board
        when it is printed.

        Returns:
            str -- The board as a string.
        '''
        board = ''
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if self.__board[row][col] == 'R':
                    board += self.__RED + \
                        self.__board[row][col] + self.__ENDC + (' ' * 2)
                elif self.__board[row][col] == 'Y':
                    board += self.__YELLOW + \
                        self.__board[row][col] + self.__ENDC + (' ' * 2)
                else:
                    board += self.__board[row][col] + (' ' * 2)
            board += '\n'
        for x in range(len(self.__col_counter)):
            board += str(x) + (' ' * 2)
        return board

    def is_filled(self):
        '''Returns whether the board is filled or not.

        Returns:
            Boolean -- True or False
        '''
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if self.__board[row][col] == self.__placeholder:
                    return False
        return True

    def put_piece(self, player):
        '''Method that puts the corresponding color piece for the
        given column from the players input.

        Arguments:
            player {Player} -- The player that will put the piece.

        Raises:
            InvalidColumnError -- raise error when the column is filled.
        '''
        col = player.get_input()
        if self.__col_counter[col] < 0:
            raise InvalidColumnError
        else:
            self.__board[self.__col_counter[col]][col] = player.color
            self.__col_counter[col] -= 1

    def __horizontal(self, color):
        '''Checkes whether there is a connect four horizontally
        for the given color.

        Arguments:
            color {Player.color} -- either 'R' or 'Y'

        Returns:
            Boolean -- either True or False
        '''
        for row in range(len(self.__board) - 1, -1, -1):
            for col in range(0, len(self.__board[row]) - 3):
                if self.__board[row][col] == color and \
                        self.__board[row][col + 1] == color and \
                        self.__board[row][col + 2] == color and \
                        self.__board[row][col + 3] == color:
                    return True
        return False

    def __vertical(self, color):
        '''Checkes whether there is a connect four vertically
        for the given color.

        Arguments:
            color {Player.color} -- either 'R' or 'Y'

        Returns:
            Boolean -- either True or False
        '''
        for col in range(len(self.__board[0])):
            for row in range(len(self.__board) - 1, -1, -1):
                if self.__board[row][col] == color and \
                        self.__board[row - 1][col] == color and \
                        self.__board[row - 2][col] == color and \
                        self.__board[row - 3][col] == color:
                    return True
        return False

    def __up_diagonal(self, color):
        '''Checkes whether there is a connect four diagonally going up
        for the given color.

        Arguments:
            color {Player.color} -- either 'R' or 'Y'

        Returns:
            Boolean -- either True or False
        '''
        for row in range(len(self.__board) - 1, 2, -1):
            for col in range(0, len(self.__board[row]) - 3):
                if self.__board[row][col] == color and \
                        self.__board[row - 1][col + 1] == color and \
                        self.__board[row - 2][col + 2] == color and \
                        self.__board[row - 3][col + 3] == color:
                    return True
        return False

    def __down_diagonal(self, color):
        '''Checkes whether there is a connect four diagonally going down
        for the given color.

        Arguments:
            color {Player.color} -- either 'R' or 'Y'

        Returns:
            Boolean -- either True or False
        '''
        for row in range(len(self.__board) - 1, 2, -1):
            for col in range(3, len(self.__board[row]), 1):
                if self.__board[row][col] == color and \
                        self.__board[row - 1][col - 1] == color and \
                        self.__board[row - 2][col - 2] == color and \
                        self.__board[row - 3][col - 3] == color:
                    return True
        return False

    def is_connect_four(self, color):
        '''Checkes whether there is a connect four for the given color.

        Arguments:
            color {Player.color} -- either 'R' or 'Y'

        Returns:
            Boolean -- either True or False
        '''
        return self.__horizontal(color) or self.__vertical(color) or \
            self.__up_diagonal(color) or self.__down_diagonal(color)

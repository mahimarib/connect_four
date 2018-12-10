from itertools import count


class Player:
    '''Defines the player, and assigns the color to the player.'''
    id = count(0)

    def __init__(self, name):
        self.name = name
        self.count = next(self.id)
        if self.count == 0:
            self.color = 'R'
        else:
            self.color = 'Y'

    def get_input(self):
        '''Asks the user for the input to put their piece in the desired
        column.

        Returns:
            int -- The column number.
        '''
        return int(input('enter column ' + self.name + ': '))

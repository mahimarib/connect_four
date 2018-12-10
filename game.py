import os
from board import Board as board
from board import InvalidColumnError
from player import Player as player

b = board()

p1 = player(input('enter name player 1: '))
p2 = player(input('enter name player 2: '))

count = 0

while not b.is_filled() and \
        b.is_connect_four(p1.color) == b.is_connect_four(p2.color):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(b)
    try:
        if count % 2 == 0:
            b.put_piece(p1)
        else:
            b.put_piece(p2)
    except (IndexError, InvalidColumnError, ValueError) as e:
        if type(e) is IndexError:
            _ = input('enter column between 0 and 6.')
        elif type(e) is InvalidColumnError:
            _ = input('enter a column that is not filled.')
        elif type(e) is ValueError:
            _ = input('invalid input enter correct column number.')
        count -= 1
    count += 1

os.system('cls' if os.name == 'nt' else 'clear')
print(b)
if b.is_connect_four(p1.color):
    print(p1.name + ' WON')
elif b.is_connect_four(p2.color):
    print(p2.name + ' WON')

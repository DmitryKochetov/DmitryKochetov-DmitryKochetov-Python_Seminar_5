# Создайте программу для игры в ""Крестики-нолики"".

# Марат, добрый день! Почему то эта задача заняла очень много времени
# подскажите более оптимальный код для строк 51-58 и почему выводится None в терминал

import random
import os
import time

field_XO = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def print_field(field_cross):
    os.system('cls')
    row = 0
    while row <= 2:
        col = 0
        while col <= 1:
            print(field_cross[row][col], end='')
            col += 1
        print(field_cross[row][col])
        row += 1



print_field(field_XO)


def is_winner_found(field_winner):

    row = 0
    col = 0
    while row <= 2:
        if ((field_winner[row][col] == 'x' and field_winner[row][col+1] == 'x' and field_winner[row][col+2] == 'x') or (field_winner[row][col] == '0' and field_winner[row][col+1] == '0' and field_winner[row][col+2] == '0')):
            return True
        row += 1

    row = 0
    col = 0
    while col <= 2:
        if ((field_winner[row][col] == 'x' and field_winner[row+1][col] == 'x' and field_winner[row+2][col] == 'x') or (field_winner[row][col] == '0' and field_winner[row+1][col] == '0' and field_winner[row+2][col] == '0')):
            return True
        col += 1

    row = 1
    col = 1
    if ((field_winner[row][col] == 'x' and field_winner[row+1][col+1] == 'x' and field_winner[row-1][col-1] == 'x') or (field_winner[row][col] == '0' and field_winner[row+1][col+1] == '0' and field_winner[row-1][col-1] == '0')):
        return True


def bot_turn(cross_field):
    nu1 = 0
    while nu1 == 0:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if (cross_field[x][y] != 'x' and cross_field[x][y] != '0'):
            cross_field[x][y] = 'x'
            nu1 = 1

    return cross_field

def player_turn(cross_field):
    player_col = int(input('Введите номер клетки по горизонтали от 0 до 2: '))
    player_row = int(input('Введите номер клетки по вертикали от 0 до 2: '))
    if (cross_field[player_row][player_col] != 'x' and cross_field[player_row][player_col] != '0'):
        cross_field[player_row][player_col] = '0'
    else:
        print('ошибка, пропуск хода')
    return cross_field

i = 0
while i <9:
    print(print_field(player_turn(field_XO)))
    # time.sleep(2)
    print(print_field(bot_turn(field_XO)))
    # time.sleep(1)
    if is_winner_found(field_XO):
        print('winner!')
        break
    i += 1

# if is_winner_found(field_XO):
#     print('winner!')

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

candies = 100

first_turn = random.randint(0, 1)
if first_turn == 0:
    print('Ходит игрок')
else:
    print('ходит компьютер')


def b_turn(cand):
    max_value = 29
    min_value = 1
    if cand < 29:
        max_value = cand
        min_value = cand
    bot_turn = random.randint(min_value, max_value)
    print(f' Тогда я заберу {bot_turn} конфет')
    cand = cand - bot_turn

    if cand <= 0:
        print('Победил компьютер, все конфеты мои, хоть я их и не ем')
        return 0
    return cand


def p_turn(cand):
    player_turn = 29
    while (player_turn > 28):
        player_turn = int(
            input(' Игрок 1, введите количество конфет, которое заберете: '))
    cand = cand - player_turn
    if cand <= 0:
        print('Игрок 1, поздравляю, вы победили. Смотрите, чтобы ничего не слиплось')
        return 0
    return cand


while candies > 0:
    
    if first_turn == 0:
        print(f'на столе лежит {candies} конфет')
        first_turn = 1
        candies = p_turn(candies)
        if candies <= 0:
            break

    print(f'на столе лежит {candies} конфет')

    candies = b_turn(candies)
    if candies <= 0:
        break

    print(f'на столе лежит {candies} конфет')

    candies = p_turn(candies)
    if candies <= 0:
        break


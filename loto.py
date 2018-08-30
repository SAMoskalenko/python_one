#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


def barrel_choise(num):
    barrel_num = [x + 1 for x in range(90)]
    random.shuffle(barrel_num)
    return (barrel_num[num])


def card():
    numbers = {random.randint(1, 90) for _ in range(15)}
    while len(numbers) < 15:
        numbers.add(random.randint(1, 90))
    numbers = list(numbers)
    string = ['  ' for _ in range(4)]
    line1 = numbers[0:5] + string
    line2 = numbers[5:10] + string
    line3 = numbers[10:15] + string
    random.shuffle(line1)
    random.shuffle(line2)
    random.shuffle(line3)
    card = [line1, line2, line3]
    return card


def print_card(player, computer):
    n = 0
    print('{} Player\'s card {}'.format('-' * 6, '-' * 6))
    while n < 3:
        print(' '.join(map(str, player[n])))
        n += 1
    print('{}'.format('-' * 26))
    n = 0
    print('{} Computer\'s card {}'.format('-' * 5, '-' * 5))
    while n < 3:
        print(' '.join(map(str, computer[n])))
        n += 1
    print('{}'.format('-' * 26))


def game():
    player_card = card()
    computer_card = card()
    num = 0
    comp_score = 0
    player_score = 0

    while num < 90:
        barrel = barrel_choise(num)
        num += 1
        print_card(player_card, computer_card)
        print('Выпал бачонок {}. Осталось {} бачонков'.format(barrel, (90 - num)))
        choise = input('Зачеркнуть цифру? (y/n)')
        for line in computer:
            for i in range(len(line)):
                if line[i] == barrel:
                    line[i] = '-'
                    comp_score += 1
        if choise == 'y':
            ch = 'not ok'
            for line in player:
                for i in range(len(line)):
                    if line[i] == barrel:
                        line[i] = '-'
                        player_score += 1
                        ch = 'ok'
            if ch == 'ok':
                print('Верно')
            else:
                print('Неверный выбор {} нет в вашей карте'.format(barrel))
                exit()
        elif choise == 'n':
            for i in range(3):
                if barrel in player[i]:
                    print('Неверный выбор {} есть в вашей карте'.format(barrel))
                    exit()
        if player_score == 15 and comp_score == 15:
            print('Ничья')
            exit()
        elif player_score == 15:
            print('Игрок победил')
            exit()
        elif comp_score == 15:
            print('Компьютер победил')
            exit()


game()

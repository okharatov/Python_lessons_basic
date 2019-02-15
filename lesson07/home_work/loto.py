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
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:
    def __init__(self, is_user):
        self.__generate_card_numbers()
        self.is_user = is_user

    def print_card(self):
        print("|".join(self.card[0]) + '\n' +
              "|".join(self.card[1]) + '\n' +
              "|".join(self.card[2]) + '\n'
              )

    def __generate_card_numbers(self):
        self.number_list = random.sample(range(1, 91), 15)

        self.card = [list(map(lambda n: str(n).rjust(2), self.__generate_line(l)))
                     for l in [sorted(self.number_list[0:5]),
                               sorted(self.number_list[5:10]),
                               sorted(self.number_list[10:15])]]

    def __generate_line(self, lis):
        l = lis.copy()
        list(map(lambda i: l.insert(i, ''), random.sample(range(0, len(l)+1), 4)))
        return l

    def try_remove(self, n):
        if n in self.number_list:
            self.number_list.remove(n)
            for i in range(3):
                if str(n).rjust(2) in self.card[i]:
                    self.card[i] = "|".join(self.card[i]).replace(
                        str(n).rjust(2), '  ').split("|")
                    if len("".join(self.card[i]).strip()) == 0:
                        return 0
            return 1
        else:
            return 2


class Game:
    @staticmethod
    def play():
        user = Card(True)
        ai = Card(False)
        bag = random.sample(range(1, 91), 90)

        for i, b in enumerate(bag):
            print(f'Новый бочонок: {b} (осталось {89-i})')
            print('------ Ваша карточка -----')
            user.print_card()
            print('-- Карточка компьютера ---')
            ai.print_card()
            answer = input('Зачеркнуть цифру? (y/n) ')

            ai_result = ai.try_remove(b)
            if answer == 'y':
                r = user.try_remove(b)
                if r is 0:
                    print('Вы победили')
                    break
                elif r is 2:
                    print('Вы проиграли')
                    break
            elif b in user.number_list or ai_result is 0:
                print('Вы проиграли')
                break


Game.play()

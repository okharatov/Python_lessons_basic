# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#
#   27  28  29  30
#   23  24  25  26
#   19  20  21  22
#   15  16  17  18     ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
# 4*(4-1)/2
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
import math

flat = int(input('Введите номер квартиры '))

#Секция - набор этажей, с одинаковым количеством квартир на этаже
section = 0
#Последний номер квартиры в секции
last_max_value = 0

#Ищим секцию с нашей квартирой
while last_max_value < flat:
    section += 1
    last_max_value += section**2

#Определяем последнюю квартиру в предыдцщей секции, для сдвигов
step = last_max_value - section**2
cur_floor_in_section = math.ceil((flat - step) / section)  #Нужный этаж в секции
max_floor_prev = int(section * (section - 1) / 2) #Последний этаж предыдущей секции

floor = cur_floor_in_section + max_floor_prev

t_number = ((flat - step)%(section))
number = t_number if t_number else section
print(floor, number)


#Рисовалка башни для проверки
# section = 0
# last_max_value = 0
# last_flat = 1
# f = 0
# _floor = 1
# print([1])
# while last_max_value < flat:
#     section += 1
#     f = last_max_value + 1
#     while last_max_value + section**2 > f:
#         _floor += 1
#         print(_floor, '|', list(range(f, f + section)))
#         f += section
#
#
#     last_max_value += section**2


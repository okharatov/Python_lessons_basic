# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

list_in = [2, -5, 8, 9, -25, 25, 4]
list_out = []

for i in list_in:
    if i > 0 and math.sqrt(i) % 1 == 0:
        list_out.append(int(math.sqrt(i))) #В примере результат написан в int

print('Задача 1',list_out)
#Конец решения, но ниже есть вопрос

### При реализации возник вопрос, почему код написанный ниже оставляет -5?
for i in list_in:
    if i < 0 or math.sqrt(i) % 1 != 0:
        list_in.remove(i)

print('Почему осталось -5?', list_in)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
import re

print('Задача 2')

# Проверка и парсинг даты
def get_date_info(date):
    pattern = '^[0-3][0-9][.][0-1][0-9][.][0-9][0-9][0-9][0-9]$'
    month_count_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # Проверка формата
    if re.match(pattern, date) != None:
        day = int(date.split('.')[0])
        month = int(date.split('.')[1])
        year = int(date.split('.')[2])

        # Проверка месяца
        if month in range(1, 13):
            max_day_by_month = month_count_day[month - 1] + 1
            # проверка на высокосный год
            max_day_by_month += year % 4 == 0  and month == 2 if 1 else 0
            if day in range(1, max_day_by_month):
                return True, day, month, year
            else:
                return False, 0, 0, 0
        else:
            return False, 0, 0, 0
    else:
        return False, 0, 0, 0

months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}
days = {
    0: '',
    1: 'первое',
    2: 'второе',
    3: 'третье',
    4: 'четвертое',
    5: 'пятое',
    6: 'шестое',
    7: 'седьмое',
    8: 'восьмое',
    9: 'девятое',
    10: 'десятое',
    11: 'одинадцатое',
    12: 'двенадцатое',
    13: 'тринадцатое',
    14: 'четырнадцатое',
    15: 'пятнадцатое',
    16: 'шестнадцатое',
    17: 'семнадцатое',
    18: 'восемнадцатое',
    19: 'девятнадцатое'
}

date = input('Введите дату в формате dd.mm.yyyy ')
date_info = get_date_info(date)

if date_info[0]:
    day = date_info[1]
    month = date_info[2]
    year = date_info[3]

    if day < 20:
        day_str = days[day]
    elif 20 <= day < 30:
        day_str = 'двадцать ' + days[day % 20]
    else:
        day_str = 'тридцать ' + days[day % 30]

    print(day_str, months[month], year, 'года')
else:
    print('Неправильная дата')



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

print('Задача 3 ')

n = int(input('Введите количество элементов списка '))
list_out = []

for i in range(n):
    list_out.append(random.randint(-100,100))
print(list_out)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('Задача 4')

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst_a = list(set(lst))
lst_b = []

for i in lst_a:
    if lst.count(i) == 1:
        lst_b.append(i)

print(f'A: {lst_a}')
print(f'B: {lst_b}')
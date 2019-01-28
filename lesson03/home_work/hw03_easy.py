# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    n_str = str(number).split('.')[0]

    n_len = 0 if n_str == '0' else len(n_str)

    big_number_str = str(number).replace('.', '')
    big_number = int(big_number_str[:ndigits + len(n_str)])
    digits = str(number).split('.')[1]
    print(big_number_str, big_number, n_len)

    if int(digits[ndigits]) < 5:
        pass
    else:
        big_number += 1

    #big_number / (


    # digits = str(number).split('.')[1][:ndigits]
    # last_digit = str(number).split('.')[1][ndigits]
    #
    # if last_digit < 5:
    #     return int(n)



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(0.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

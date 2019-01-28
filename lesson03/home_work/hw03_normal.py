# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def prev_sum(list):
    return sum(list[::-1][:2])

def fibonacci(n, m):
    f_list = [1,1]
    for _ in range(m - 2):
        f_list.append(prev_sum(f_list))
    return  f_list[n - 1:]

print(fibonacci(3, 8))
# //[2, 3, 5, 8, 13, 21]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    result = []
    cnt = len(origin_list)

    for _ in range(cnt):
        result.append(origin_list.pop(origin_list.index(min(origin_list))))
    return result


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func, enum):
    result = []
    for i in enum:
        if func(i):
            result.append(i)

    return result


f = lambda x: x == 2

print(my_filter(f, [2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math

def get_length(a1, a2):
    return math.sqrt((a2[0]-a1[0])**2+(a2[1]-a1[1])**2)

def is_parallelogram(a_list):
    len_list = []
    for i in range(4):
        for j in range(i + 1, 4):
            len_list.append(get_length(a_list[i],a_list[j]))

    group_cnt = [int(len_list.count(x) >= 2) for x in set(len_list)]
    return sum(group_cnt) == 2


test1 = [[1,5],[5,5],[0,4],[4,4]]
test2 = [[1,1],[1,5],[5,1],[5,5]]
test3 = [[1,1],[1,5],[5,1],[5,8]]
print(is_parallelogram(test1))
print(is_parallelogram(test2))
print(is_parallelogram(test3))
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil as s
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("ls - отображение полного пути текущей директории")
    print("cd - меняет текущую директорию на указанную")
    print("cp - создает копию указанного файла")
    print("rm - удаляет указанный файл")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def my_ls():
    print(os.getcwd())

def my_cd():
    try:
        os.chdir(dir_name)
        print('директория успешно изменена')
    except Exception:
        print('директория не изменена')

def my_cp():
    try:
        s.copy(dir_name, '(copy)' + dir_name)
        print(f'файл {dir_name} успешно скопирован')
    except Exception:
        print('неудалось скопировать файл')


def my_rm():
    if 'y' == input(f'Вы уверены, что хотите удалить файл {dir_name}? (y/n)'):
        try:
            os.remove(dir_name)
            print(f'файл {dir_name} успешно удален')
        except Exception:
            print('неудалось удалить файл')

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": my_ls,
    "cd": my_cd,
    "cp": my_cp,
    "rm": my_rm
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")


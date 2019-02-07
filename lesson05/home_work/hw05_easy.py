# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil as s

def make_dir(name):
    try:
        os.mkdir(name)
        print(f'Директория {name} успешно создана')
    except Exception:
        print(f'Директорию {name} создать невозможно')

def remove_dir(name):
    try:
        os.rmdir(name)
        print(f'Директория {name} успешно удалена')
    except Exception:
        print(f'Директорию {name} удалить невозможно')



if __name__ == "__main__":
    dir_list = ["dir" + str(i + 1) for i in range(9)]
    [make_dir(d) for d in dir_list]
    [remove_dir(d) for d in dir_list]
    # [os.mkdir(d) for d in dir_list]
    # [os.rmdir(d) for d in dir_list]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#1 - Показываем только папки
#2 - Показываем все

def show_dir(only_dir):
    print(list(filter(lambda x: os.path.isdir(x) or not only_dir, os.listdir())))

if __name__ == "__main__":
    show_dir(True)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
s.copy(sys.argv[0], '(copy)' + sys.argv[0])

# Функция для normal
def change_dir(path):
    try:
        os.chdir(path)
        print(f'Переход в директорию {path} успешно выполнен')
    except Exception:
        print(f'Переход в директорию {path} невозможн')

if __name__ == "__main__":
    dir_name = "dir11"

    make_dir(dir_name)
    change_dir(dir_name)
    print(os.getcwd())
    
    change_dir(os.path.dirname(os.getcwd()))
    remove_dir(dir_name)
    change_dir(dir_name)

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

for i in range(1, 10):
    try:
        os.mkdir('dir_{}'.format(i))
    except FileExistsError:
        print('Дирректория dir_{} уже существует'.format(i))

for i in range(1, 10):
    try:
        shutil.rmtree('dir_{}'.format(i))
    except FileNotFoundError:
        print('Дирректория dir_{} не существует'.format(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

for name in os.listdir():
    if os.path.isdir(name):
        print(name)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ != '__main__':
    filename = sys.argv[0]
    newfile = filename + '.copy.py'
    shutil.copy(filename, newfile)


# для Hard



def make_dir(name):
    try:
        os.mkdir(name)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('Дирректория {} уже существует'.format(name))

def del_dir(name):
    try:
        shutil.rmtree(name)
        print('директория {} удалена'.format(name))
    except FileNotFoundError:
        print('Дирректория {} не существует'.format(name))

def in_dir():
    for _ in os.listdir():
        print(_)



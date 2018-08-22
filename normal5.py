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


import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


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


def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(file_path):
        file_path_copy = file_path + '.copy'
        shutil.copy(file_path, file_path_copy)
        print('файл {} скопирован'.format(dir_name))
    else:
        print('{} не является файлом'.format(dir_name))


def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(file_path):
        answer = input('Вы действительно хотите удалить файл? (Y/N): ')
        if answer == 'Y':
            os.remove(file_path)
            print('файл {} удален'.format(dir_name))
        else:
            print('отмена удаления файла {}'.format(dir_name))
    else:
        print('{} не является файлом'.format(dir_name))


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_path):
        os.chdir(dir_path)
        print('директория изменена на {}'.format(dir_name))
    else:
        print('{} не существует'.format(dir_name))

def path_to_dir():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": path_to_dir
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

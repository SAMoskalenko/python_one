# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
n = 1
print(fruits)
for i in fruits:
    print('{}. {}'.format(n, i))
    n += 1

print()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = [1, 2, 3, 4, 'коготь', 'нож']
spisok2 = [3, 4, 5, 6, 'коготь']

spisok1 = list(set(spisok1) - set(spisok2))

print(spisok1)

print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list1 = [1, 2, 3, 4, 5, 6]
n = 0
for elem in list1:
    if elem % 2 == 0:
        list1[n] = int(elem / 2)
    else:
        list1[n] = int(elem * 2)
    n += 1
print(list1)

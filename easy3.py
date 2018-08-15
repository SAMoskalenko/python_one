# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def about(name, age, city):
    print('{} , {} года(а), проживает в городе {}'.format(name, age, city))


about('Сергей', 37, 'Москва')

print()


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def biggest(num1, num2, num3):
    biggest = num1
    if num2 > biggest:
        biggest = num2
    elif num3 > biggest:
        biggest = num3
    return biggest


print(biggest(2, 4, 3))

number = (1, 2, 3, 4)
print(number[1])


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def biggest_line(*lines):
    num = 0
    bl = str
    for line in lines:
        if len(line) > num:
            num = len(line)
            bl = str(line)
    return bl


print(biggest_line((1, 3, 4, 5), ('ghbdtn', 'ghjsdg', 3), ('dqwgfgceuy')))

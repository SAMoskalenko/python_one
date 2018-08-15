# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


player = {'name': input('введте имя игрока: '), 'health': 100, 'damage': 50}
enemy = {'name': input('введте имя противника: '), 'health': 100, 'damage': 50}


def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']
    return person2


print()

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player = {'name': input('введте имя игрока: '), 'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'name': input('введте имя противника: '), 'health': 100, 'damage': 50, 'armor': 1.2}

file = open('{}.txt'.format(player['name']), 'w+', encoding='UTF-8')
for key, value in player.items():
    file.write('{} : {} \n'.format(key, value))
file.seek(0)
first_player = {}
for line in file:
    name, symb, mean = line.split()
    first_player[name] = mean
file.close()

file = open('{}.txt'.format(enemy['name']), 'w+', encoding='UTF-8')
for key, value in enemy.items():
    file.write('{} : {} \n'.format(key, value))
file.seek(0)
second_player = {}
for line in file:
    name, symb, mean = line.split()
    second_player[name] = mean
file.close()

first_player['health'], second_player['health'] = float(first_player['health']), float(second_player['health'])
first_player['damage'], second_player['damage'] = float(first_player['damage']), float(second_player['damage'])
first_player['armor'], second_player['armor'] = float(first_player['armor']), float(second_player['armor'])


def shield(person1, person2):
    person2['health'] = person2['health'] + person1['damage'] / person2['armor']
    return person2


pl = 1
while pl > 0:
    if pl % 2 != 0:
        attack(first_player, second_player)
        print(first_player, second_player)
        shield(first_player, second_player)
        print(first_player, second_player)
        if second_player['health'] <= 0:
            print('{} победил, осталось {} едениц здоровья'.format(first_player['name'], first_player['health']))
            break
    else:
        attack(second_player, first_player)
        print(first_player, second_player)
        shield(second_player, first_player)
        print(first_player, second_player)
        if first_player['health'] <= 0:
            print('{} победил, осталось {} едениц здоровья'.format(second_player['name'], second_player['health']))
            break
    pl += 1
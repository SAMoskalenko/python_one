# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Fabric:

    def purchase(self):
        print('Закупка сырья')

    def sewing(self):
        print('Пошив игрушки')

    def painting(self):
        print('Окраска игрушки')

    def creating(self, name, color, type):
        toy = Toy(name, color, type)
        return toy


class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type
        print(self.name, self.color, self.type)

    # Задача - 2


# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Fabric:

    def purchase(self):
        print('Закупка сырья')

    def sewing(self):
        print('Пошив игрушки')

    def painting(self):
        print('Окраска игрушки')

    def creating(self, name, color, type):
        if type == 'животное':
            toy = Animal(name, color, type)
        elif type == 'персонаж мультфильма':
            toy = Cartoon(name, color, type)
        return toy


class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type
        print(self.name, self.color, self.type)


class Animal(Toy):
    None


class Cartoon(Toy):
    None


fab = Fabric()
fab.creating('Лев', 'Желтый', 'персонаж мультфильма')

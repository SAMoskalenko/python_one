# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self):
        return self.damage

    def defence(self, attack):
        self.health = self.health - attack // self.armor


class Player(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def action(self, player, enemy):
        attacker = player
        while player.health > 0 and enemy.health > 0:
            if attacker == player:
                enemy.defence(player.attack())
                attacker = enemy
            else:
                player.defence(enemy.attack())
                attacker = player

        if player.health > 0:
            print('{} победил!'.format(player.name))
        else:
            print('{} победил!'.format(enemy.name))


pl1 = Player('Boris', 100, 50, 0.6)
pl2 = Enemy('Johnson', 120, 50, 0.6)

game = Game(pl1, pl2)
game.action(pl1, pl2)

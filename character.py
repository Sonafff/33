class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name, health, damage, defence=0):
        self.name = name
        self.damage = damage
        self.health = health
        self.defence = defence

    def show_information(self):
        print(self.__str__())

    def show_info(self):
        print(f' = {self.name} = \n'
              f'Health = {self.health}\n'
              f'Damage = {self.damage}\n'
              f'Defence = {self.defence}\n')

    def take_damage(self, damage):
        self.health -= damage
        return damage

    def attack(self, target):
        return target.take_damage(self.damage)
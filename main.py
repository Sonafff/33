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

    def is_alive(self):
        return self.health > 0

player1 = Character('Kristixx_', health=10, damage=2)
player1.show_info()

player2 = Character('Sonaff', health=15, damage=3)
player2.show_info()

while player1.is_alive() and player2.is_alive():
    p1_damage = player1.attack(player2)
    if player2.is_alive():
        print(f'{player1.name} атакував {player2.name} і наніс {p1_damage} шкоди')
    else:
        print(f'{player1.name} атакував {player2.name}, але {player2.name} вже мертвий!')

    p2_damage = player2.attack(player1)
    if player1.is_alive():
        print(f'{player2.name} атакував {player1.name} і наніс {p2_damage} шкоди')
    else:
        print(f'{player2.name} атакував {player1.name}, але {player1.name} вже мертвий!')

print(f'Кінець бою!')
print(f'Залишилось здоров`я у {player1.name}: {player1.health}')
print(f'Залишилось здоров`я у {player2.name}: {player2.health}')


player1 = Character('Kristixx_', health=10, damage=2)
player2 = Character('Sonaff', health=10, damage=3)

while player1.health > 0 and player2.health > 0:
    p1_damage = player1.attack(player2)
    print(f'{player1.name} атакував {player2.name} і наніс {p1_damage} шкоди.')
    if player2.health <= 0:
        print(f'{player2.name} помер!')
        break

    p2_damage = player2.attack(player1)
    print(f'{player2.name} атакував {player1.name} і наніс {p2_damage} шкоди.')
    if player1.health <= 0:
        print(f'{player1.name} помер!')
        break

print(player1.show_info())
print(player2.show_info())


p1_damage = player1.attack(player2)
print (f' {player1. name} атакував {player2.name}'
       f' і наніс {p1_damage} шкоди')
p2_damage = player2.attack(player1)
print(f' {player2. name} атакував {player1.name}'
      f' і наніс {p2_damage} шкоди')

print(player1, player2, sep='\n')
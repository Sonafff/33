from character import Character

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
       f'і наніс {p1_damage} шкоди')
p2_damage = player2.attack(player1)
print(f' {player2. name} атакував {player1.name}'
      f'і наніс {p2_damage} шкоди')

print(player1, player2, sep='\n')
import os
from classes.character import Character

enemy = Character(name="Enemy", healt=100, base_damage=3)

def battle(hero: Character):
  while True:
    os.system('cls')

    hero.attack(enemy)
    print(f"Healt of {enemy.name}: {enemy.healt}")
    input()
    
    if enemy.healt <= 0:
      print(f"{enemy.name} has been defeat by {hero.name}")
      if enemy.weapon.damage > 0:
        enemy.drop()
      break

    enemy.attack(hero)
    print(f"Healt of {hero.name}: {hero.healt}")
    input()

    if hero.healt == 0:
      print(f"{hero.name} has been defeat by {enemy.name}")
      if hero.weapon.damage > 0:
        hero.drop()
      break

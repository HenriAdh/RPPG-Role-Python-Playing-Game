import os
from classes.character import Character 
from classes.weapon import Weapon
from pages.battle import battle
from pages.equip import equip

os.system('cls')

score = 0
level = 0

short_bow = Weapon(name="short bow", weapon_type="ranged", damage=8, value=10)
iron_sword = Weapon(name="iron sword", weapon_type="sharp", damage=10, value=15)

print('Wellcome warrior! whats your name? ')
name = input()

hero = Character(name=name, healt=100, base_damage=5)

os.system('cls')
print(f"Nice to meet you {hero.name}, choose your initial weapon:\n")
print(f"Current Gold: {hero.gold}\n")
print("----------------------------------------------")
print("[1] Short Bow | [2] Iron Sword | [any] Without")
print(" -damage: 8   |  -damage: 10   |  -damage: 5  ")
print(" -value: $10  |  -value: $15   |  -value: $0  ")

chosen_weapon = input()

weapons = {
  '1': short_bow,
  '2': iron_sword,
}

if chosen_weapon in weapons:
  hero.buy(weapon=weapons[chosen_weapon])

while True:
  print(f"Would do you like do?")
  print(f"[1] Battle")
  print(f"[2] Equip")
  print(f"[3] View stats")
  print(f"[4] End")

  action = input('\n')
  if int(action) in [1, 2, 3, 4]:
    break

def temp(hero: Character):
  input(f"\n{hero.name}\n")

actions = {
  1: battle,
  2: equip,
  3: temp,
  4: temp,
}

actions[int(action)](hero=hero)
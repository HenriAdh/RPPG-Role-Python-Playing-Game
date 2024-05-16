from classes.weapon import Weapon, default_weapon

class Character:
  def __init__(self, name: str, healt: int, base_damage: int) -> None:
    self.name = name
    self.base_healt = healt
    self.healt = healt
    self.base_damage = base_damage
    self.damage = base_damage
    self.weapon = default_weapon
    self.gold = 10
    self.bag: list[Weapon] = []
    self.level = 0

  def attack(self, target) -> None:
    if self.weapon.damage == 0:
      damage = self.base_damage
    else:
      damage = self.weapon.damage
    target.healt -= damage

    target.healt = max(target.healt, 0)
    print(f"{self.name} dealt {damage} to {target.name} with {self.weapon.name}")

  def equip(self, weapon: Weapon) -> None:
    self.weapon = weapon
    print(f"{self.name} equipped {weapon.name}!")

  def drop(self) -> None:
    print(f"{self.name} dropped {self.weapon.name}!")
    self.weapon = default_weapon

  def earn(self, gold) -> None:
    print(f"{self.name} earned {gold} gold.")
    self.gold += gold

  def buy(self, weapon: Weapon) -> None:
    self.gold -= weapon.value
    self.bag.append(weapon)
    print(f"{self.name} bought the weapon: {weapon.name}. Current Gold: {self.gold}")
    input()

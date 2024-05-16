class Weapon:
  def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
    self.name = name
    self.weapon_type = weapon_type
    self.damage = damage
    self.value = value

default_weapon = Weapon(name='your self hands', weapon_type='none', damage=0, value=0)
from classes.character import Character

def equip(hero: Character):
  print("Escolha o equipamento desejado:")
  for x in range(len(hero.bag)):
    print(f"[{x + 1}] {hero.bag[x].name}")
  input("\n")
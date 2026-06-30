#클래스

class Unit:
  def __init__ (self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print(f"[생성]{self.name} / 체력 : {self.hp} / 공격력 : {self.damage}")
    
# soldier1 = Unit("보병1", 40, 5)
# soldier2 = Unit("보병2", 40, 5)
# soldier3 = Unit("보병3", 40, 5)
# tank1 = Unit("탱크1", 150, 30)
# tank2 = Unit("탱크2", 150, 30)

# tank1.fly = False
# soldier1.fly = False
# print(f"{tank1.name} {tank1.hp} {tank1.damage} {tank1.fly}")
# print(f"{soldier1.name} {soldier1.hp} {soldier1.damage} {soldier1.fly}")

class AttackUnit:
  def __init__ (self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print(f"[생성]{self.name} / 체력 : {self.hp} / 공격력 : {self.damage}")
  def attack(self, location):
    print(f"[공격]{self.name} / 공격방향 : {location} / 데미지 : {self.damage}")
  def damaged(self, damage):
    self.hp -= damage
    if self.hp <= 0 : print(f"[파괴]{self.name} / 받은데미지 : {damage} / 현재체력 : 0")
    else: print(f"[방어]{self.name} / 받은데미지 : {damage} / 현재체력 : {self.hp}")

fireSoldier1 = AttackUnit("화염병1", 50, 10)

fireSoldier1.attack("2시")
fireSoldier1.damaged(30)

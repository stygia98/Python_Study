# 상속

class Unit:
  def __init__ (self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"[생성]{self.name} / 체력 : {self.hp} / 이동속도 : {self.speed}")

nurse1 = Unit("간호병1", 40, 5)
nurse2 = Unit("간호병2", 40, 5)

class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage):
    # super().__init__(name, hp, speed)
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
  def attack(self, location):
    print(f"[공격]{self.name} / 공격방향 : {location} / 데미지 : {self.damage}")
  def damaged(self, damage):
    self.hp -= damage
    if self.hp <= 0 : print(f"[파괴]{self.name} / 받은데미지 : {damage} / 현재체력 : 0")
    else: print(f"[방어]{self.name} / 받은데미지 : {damage} / 현재체력 : {self.hp}")

fireSoldier1 = AttackUnit("화염병1", 50, 10, 10)

fireSoldier1.attack("2시")
fireSoldier1.damaged(60)

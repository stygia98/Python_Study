
class Unit:
  def __init__ (self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"[생성]{self.name} / 체력 : {self.hp}")
  def move(self, location):
    print(f"[이동]{self.name} / {location}방향으로 이동 / 이동속도 {self.speed}")

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
    
class Flyable:
  def __init__(self, flying_spd):
    self.flying_spd = flying_spd
  def fly(self, location):
    print(f"[이동]속도 : {self.flying_spd} / 이동방향 : {location}")

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, speed, damage, flying_spd):
    AttackUnit.__init__(self, name, hp, speed, damage)
    Flyable.__init__(self, flying_spd)
  def move(self, location):
    print(f"[이동]{self.name} / {location}방향으로 이동 / 이동속도 {self.flying_spd}")

interceptor1 = FlyableAttackUnit("요격기1", 300, 0, 80, 200)
# interceptor1.attack(2)
# interceptor1.damaged(20)
# interceptor1.fly(2)
interceptor1.move(3)

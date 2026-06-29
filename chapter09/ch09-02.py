class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    # print(f"{self.name} 생성 / 체력: {self.hp} / 공격력: 0 / 이동속도: {self.speed}")
  def move(self, location):
    print(f"{self.name} : [이동] {location} 방향으로 이동")

class AttackUnit(Unit):
  def __init__(self, name, hp, damage, speed):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
    print(f"{self.name} 생성 / 체력: {self.hp} / 공격력: {self.damage} / 이동속도: {self.speed}")
  #멤버함수
  def attack(self, location):
    print(f"{self.name} : [공격] {location} 방향으로 {self.damage} 의 공격")

  def damaged(self, damage):
    print(f"{self.name} : [방어] 상대로부터 {damage} 의 공격")
    self.hp = self.hp - damage
    print(f"{self.name} : 남은체력 {self.hp}")
    if self.hp <= 0: print(f"{self.name} : 유닛 파괴됨")
    
  def move(self, location):
    print(f"{self.name} : [이동] {location} 방향으로 이동 / 공격력 : {self.damage}")

solder1 = AttackUnit("보병1", 40, 5, 10)
solder2 = AttackUnit("보병2", 40, 5, 10)
solder3 = AttackUnit("보병3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 150, 35, 30)
tank2 = AttackUnit("탱크2", 150, 35, 30)

attack_unit = []
attack_unit.append(solder1)
attack_unit.append(solder2)
attack_unit.append(solder3)
attack_unit.append(tank1)
attack_unit.append(tank2)

for unit in attack_unit:
  unit.move(10)
  # unit.attack(2)
  
# for unit in attack_unit:
#   unit.damaged(10)

#클래스

class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"{self.name} 생성 / 체력: {self.hp} / 공격력: 0 / 이동속도: {self.speed}")

class AttackUnit:
  def __init__(self, name, hp, damage, speed):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.speed = speed
    print(f"{self.name} 생성 / 체력: {self.hp} / 공격력: {self.damage} / 이동속도: {self.speed}")

  #멤버함수
  def attack(self, location):
    print(f"{self.name} : {location} 방향으로 {self.damage} 의 공격")

  def damaged(self, damage):
    print(f"{self.name} : 상대로부터 {damage} 의 공격")
    self.hp = self.hp - damage
    print(f"{self.name} : 남은체력 {self.hp}")
    if self.hp <= 0: print(f"{self.name} : 유닛 파괴됨")

solder1 = AttackUnit("보병1", 40, 5, 10)
solder2 = AttackUnit("보병2", 40, 5, 10)
solder3 = AttackUnit("보병3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 150, 35, 30)
tank2 = AttackUnit("탱크2", 150, 35, 30)

# solder1.attack(10)
# solder2.attack(10)
# solder3.attack(10)
# tank1.attack(10)
# tank2.attack(10)

attack_list = []
attack_list.append(solder1)
attack_list.append(solder2)
attack_list.append(solder3)
attack_list.append(tank1)
attack_list.append(tank2)

for unit in attack_list:
  unit.attack(10)

# solder1.damaged(5)
# solder2.damaged(5)
# solder3.damaged(5)
# tank1.damaged(10)
# tank2.damaged(10)

for unit in attack_list:
  unit.damaged(10)

airUnit1 = AttackUnit("전투기1", 200, 30, 40)
airUnit1.fly = True

if airUnit1.fly == True:
  print(f"{airUnit1.name} {airUnit1.hp} {airUnit1.damage} {airUnit1.speed} 공중유닛:{airUnit1.fly}")
  
import string


class Person:
    name:string
    surname:string
    penis:int
    colour:string
    hp:int
    dmg:int



def Hit(PAttack:Person,PDef:Person):
    PDef.hp = PDef.hp - PAttack.dmg
    print(PAttack.hp, PDef.hp)


Valera = Person()
Valera.name = "Valera"
Valera.surname = "Joposos"
Valera.hp = 100
Valera.dmg = 10
Ionut = Person()
Ionut.name = "Ionut"
Ionut.hp = 100
Ionut.dmg = 20
Hit(PAttack=Ionut, PDef= Valera)

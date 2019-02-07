class Character():
    name=""
    sex=""
    health=0
    stamina=0
    mana=0
def display_Character(my_character):
    print(my_character.name,my_character.sex,my_character.health,my_character.stamina,my_character.mana)
gammy=Character()
gammy.name="Gammy"
gammy.sex="Male"
gammy.health="Health:1"
gammy.stamina="Stamina:1"
gammy.mana="Mana:1"
display_Character(gammy)
print('')
damian=Character()
damian.name="Damian"
damian.sex="Male"
damian.health="Health:1000"
damian.stamina="Stamina:1000"
damian.mana="Mana:1000"
display_Character(damian)
from battleship import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "dragon", "cost": 10, "dmg": 80},
         {"name": "hippo", "cost": 10, "dmg": 70}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY attacks" + bcolors.ENDC)

while running:
   # player.choose_action()
    player.choose_magic()

    choice = input("choose action:")
    index = int(choice) - 1
    #print("You chose:", choice)
    print("you chose", player.get_spell_name(int(index)))

    running = False
#print(player.generate_damage())
#print(player.generate_damage())
#print(player.generate_damage())

#print(player.generate_spell_damage(0))
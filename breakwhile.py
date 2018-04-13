import random

raone = 300
goneh = 100
gonel = 80

while raone > 0:
    damage = random.randrange(gonel, goneh)
    raone = raone - damage

    if raone <=30:
        raone = 30


    print("raone damage is", damage, "current raone health is", raone)

    if raone > 30:
        continue

    print("raone u have less life. pls search life tablet")
    break



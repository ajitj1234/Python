
class Raone:
    powerl = 60
    powerh = 100
    powerl1 = 80
    powerh1 = 200
    hp = 500
'''
    #def __init__(self, powerl, powerh):
     #   self.powerl = powerl
      #  self.powerh = powerh
'''
    def getpower(self):
        print(self.powerl, self.powerh)
        print(self.powerl1, self.powerh1)

    def getHp(self):
        print(self.hp)

power1 = Raone()
#power1 = Raone(60, 100)
power1.getpower()
power1.getHp()


#from classes.enemy import Enemy

power2 = Raone()
power2.getpower()
power2.getHp()
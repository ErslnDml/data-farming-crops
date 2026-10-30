
from farm.crop import Crop

'''class Rice():
    def __init__(self):
        self.grains=0
    def water(self):
        self.grains+=5
    def ripe(self):
       return self.grains >=15
    def transplant(self):
        self.grains+=10'''


'''rice=Rice()
print(rice.grains)

rice.water()
print(rice.grains)
print(rice.ripe())

rice.water()
print(rice.grains)
print(rice.ripe())

rice.transplant()
print(rice.ripe())'''


class Rice(Crop):
 def water(self):
     self.grains +=5
 def transplant(self):
       self.grains += 10


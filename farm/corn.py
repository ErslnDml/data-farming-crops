
class Corn:
    def __init__(self):
        self.grains=0
    def water(self):
        self.grains+=10
    def ripe(self):
       return  self.grains >= 15 


'''corn1=Corn()
print(corn1.ripe())

corn1.water()
print(corn1.grains)
print(corn1.ripe())

corn1.water()
print(corn1.grains)
print(corn1.ripe())'''


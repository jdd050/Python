# minecraft triangulation script
# calculates where a stronghold is given:
# distance traveled (n/s or w/e)
# heading

'''
formulas: https://www.youtube.com/@BlackNinja745Minecraft
'''
import numpy

class Main:
    
    def __init__(self) -> None:
        # get required information for formulas
        self.displacement =  int(input("Blocks traveled:\n"))
        self.h1 = float(input("First heading:\n"))
        self.h2 = float(input("Second heading:\n"))
        self.cardinal_direction = input("Cardinal direction (n/s/e/w):\n")
        return None
    
    def findStronghold(self) -> tuple:
        # north / south
        if (self.cardinal_direction == 'n') or (self.cardinal_direction == 's'):
            x = -((self.displacement)/(numpy.tan(90-numpy.deg2rad(self.h1)) - numpy.tan(90-numpy.deg2rad(self.h2))))
            z = ((self.displacement * numpy.tan(numpy.deg2rad(self.h1)))/(numpy.tan(90-numpy.deg2rad(self.h1)) - numpy.tan(90-numpy.deg2rad(self.h2))))
        # east / west
        else:
            x = ((self.displacement * numpy.tan(numpy.deg2rad(self.h1)))/(numpy.tan(numpy.deg2rad(self.h1)) - numpy.tan(numpy.deg2rad(self.h2))))
            z = -((self.displacement)/(numpy.tan(numpy.deg2rad(self.h1)) - numpy.tan(numpy.deg2rad(self.h2))))
        return (x,z)
    
main = Main()
print(main.findStronghold())

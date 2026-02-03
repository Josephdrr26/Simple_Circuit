from bus import Bus

class Resistor:
    #Attributes
    def __init__(self, name:str, bus1: Bus, bus2:Bus, r:float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = self.calc_g()
    #Methods
    def calc_g(self):
       g = 1/ self.r
       return g

# if __name__ == '__main__':
#     #testing class
#     R1 = Resistor('R1', 'A', 'B', 5)
#     print(R1.name, R1.bus1, R1.bus2, R1.r, R1.g)
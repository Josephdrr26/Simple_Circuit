from bus import Bus
class Load:
    #Attributes
    def __init__(self, name: str, bus1: Bus, p: float, vnom: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.vnom = vnom
        self.g = self.calc_g()
    #Method
    def calc_g(self):
        g = self.p / pow(self.vnom, 2)
        return g

"""Testing Class
L1 = Load("L1", "B", 50, 0)
testing_v = 100
L1.calc_g(testing_v)
print("The conductance of the load R is", L1.g)"""

class Load:
    #Attributes
    def __init__(self, name: str, bus1: str, p: float, q: float, g: float = 0.0):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
        self.g = None
    #Method
    def calc_g(self, v: float):
        self.g = self.p / pow(v,2)

"""Testing Class
L1 = Load("L1", "B", 50, 0)
testing_v = 100
L1.calc_g(testing_v)
print("The conductance of the load R is", L1.g)"""

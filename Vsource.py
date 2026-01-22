from Bus import Bus

class Vsource:
    #Attributes
    def __init__(self, name:str, bus1: Bus, v:float):
        self.name = name
        self.bus1 = bus1
        self.v = v
        self.bus1.set_bus_v(v)
"""Testing Class
V1 = Vsource('V1', 'A', 120)
print(V1.name, V1.bus1, V1.v)"""
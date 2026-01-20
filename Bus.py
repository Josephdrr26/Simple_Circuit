class Bus:
    #Attributes:
    def __init__(self, name: str, v: float = 0.0):
        self.name = name
        self.v = v
    #Methods:
    def set_bus_v(self, bus_v: float):
        self.v = bus_v
"""Testing Class
b1 = Bus("A", 0.0)
b1.set_bus_v(120)
print("This is Bus", b1.name, "and v is", b1.v )"""
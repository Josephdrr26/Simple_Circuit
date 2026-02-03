from typing import Dict
from bus import Bus
from Load import Load
from Vsource import Vsource
from Resistor import Resistor

class Circuit:
    #Attributes
    def __init__(self,name: str):
        self.name = name
        self.buses: Dict[str, Bus] = {}
        self.resistors: Dict[str, Resistor] = {}
        self.loads: Dict[str, Load] = {}
        self.vsource = None
        self.i: float = 0.0
    #Methods
    def add_bus(self, bus: str):
        objbus = Bus(bus)
        self.buses[bus] = objbus
        return objbus
    def add_resistor_element(self, name: str, bus1_name: str, bus2_name: str, r:float):
        try:
            bus1 = self.buses[bus1_name]
            bus2 = self.buses[bus2_name]
        except KeyError as e:
            raise ValueError(f"Bus '{e.args[0]}' does not exist in the circuit")

        resistor = Resistor(name, bus1, bus2, r)
        self.resistors[name] = resistor

    def add_load_element(self, name: str, bus1_name: str, p: float, v:float):
        #Create the load
        bus1 = self.buses[bus1_name]
        load = Load(name, bus1, p, 100)
        self.loads[name] = load
    def add_vsource_element(self, name: str, bus1: Bus, v:float):
        self.vsource = Vsource(name, bus1, v)
    def set_i(self, i: float):
        self.i = i
    def print_nodal_voltage(self):
        for bus in self.buses:
            bus_obj = self.buses[bus]
            print(bus_obj.name, bus_obj.v)
    def print_circuit_current(self):
        print("The circuit current is", self.i)
from Circuit import Circuit

class Solution:
    def __init__(self, Circuit):
        self.Circuit = Circuit

    def do_power_flow(self):
        circuit_pf = self.Circuit
        #Source V at Bus A
        Va = circuit_pf.vsource.v
        circuit_pf.add_bus("A")
        circuit_pf.buses["A"].set_bus_v(Va)

        #Extracting  resistor and load value
       # circuit_pf.add_resistor_element("R1", "A", "B", 0.5)
        for key in circuit_pf.resistors:
            #print(circuit_pf.resistors[key].r)
            Rab = circuit_pf.resistors[key].r
            Gab = circuit_pf.resistors[key].g
            break

        for key in circuit_pf.loads:
            #print(circuit_pf.loads[key].p)
            load = circuit_pf.loads[key].p
            Gload = circuit_pf.loads[key].g
            break

        #Calculating circuit I
        I = Va / ((1/Gab)+ (1/Gload))
        circuit_pf.i = I
        # B Bus Voltage
        Vb = I * (1/Gload)
        circuit_pf.buses["B"].set_bus_v(Vb)

"""if __name__ == '__main__':
    Testc = Circuit("Test Circuit")
    test = Solution(Testc)
    test.do_power_flow()"""
class Solution:
    def __init__(self, Circuit):
        self.Circuit = Circuit

    def do_power_flow(self):
        circuit_pf = self.Circuit
        #Source V at Bus A
        Va = circuit_pf.vsource.v
        circuit_pf.buses["A"].set_bus_voltage(Va)

        #Extracting  resistor and load value
        resistor = circuit_pf.resistor.r
        load = circuit_pf.load.p

        #Calculate the conductance for R1 and load R
        g_r = resistor.g
        g_l = load.g

        #Calculating circuit I
        I = Va / ((1/g_r)+ (1/g_l))

        # B Bus Voltage
        Vb = I * (1/g_l)
        circuit_pf.buses["B"].set_bus_voltage(Vb)


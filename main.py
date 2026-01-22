from Circuit import Circuit
from Solution import Solution

def main():
    #Defining Circuit
    circuit = Circuit("Simple Circuit")
    #Adding Buses
    bus_A = circuit.add_bus("A")
    circuit.add_bus("B")

    #Adding voltage source
    circuit.add_vsource_element("Va", bus_A, 100)

    # Adding resistor Rab
    circuit.add_resistor_element("Rab", "A", "B", 5)

    #Adding load
    circuit.add_load_element("Lb", "B", 2000, 100)

    #Creating a solution object
    solution = Solution(circuit)
    solution.do_power_flow()

    #Displaying calculated nodal V and I
    circuit.print_nodal_voltage()
    circuit.print_circuit_current()

main()
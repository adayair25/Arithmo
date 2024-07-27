
def calculate_voltage(resistance, current):
    voltage = current * resistance
    return print(f"Voltage: {voltage} V")

def calculate_current(voltage, resistance):
    current = voltage / resistance
    return print(f"Current: {current} A")

def calculate_resistance(voltage, current):
    resistance = voltage / current
    return print(f"Resistance: {resistance} ohms")

# Example of use
calculate_voltage(10, 2)

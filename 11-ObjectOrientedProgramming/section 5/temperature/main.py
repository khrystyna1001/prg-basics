import temperature

# Create a thermometer
# Turn thermometer on
# Measure temperature
# Display temperature
# Turn thermometer off

def main():
    thermometer = temperature.Thermometer(temperature.temperature)
    thermometer.turn_on()
    thermometer.measure()
    thermometer.turn_off()

if __name__ == "__main__":
    main()
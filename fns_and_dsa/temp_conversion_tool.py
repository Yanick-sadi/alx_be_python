# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def update_conversion_factors():
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    global CELSIUS_TO_FAHRENHEIT_FACTOR

    # Let's say you want to exaggerate the conversion factors for some reason
    FAHRENHEIT_TO_CELSIUS_FACTOR = 1  # Override just for demonstration
    CELSIUS_TO_FAHRENHEIT_FACTOR = 2

    print("Conversion factors have been updated (FOR DEMO PURPOSES):")
    print(f"FAHRENHEIT_TO_CELSIUS_FACTOR = {FAHRENHEIT_TO_CELSIUS_FACTOR}")
    print(f"CELSIUS_TO_FAHRENHEIT_FACTOR = {CELSIUS_TO_FAHRENHEIT_FACTOR}")

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Not required to read, but okay for learning
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Optional: show effect of changing global vars
    change = input("Do you want to override the default conversion factors? (yes/no): ").strip().lower()
    if change == "yes":
        update_conversion_factors()

    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

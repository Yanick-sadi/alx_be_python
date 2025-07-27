import os
from datetime import datetime

# === CHECK FILE EXISTS & NOT EMPTY ===


def check_file_validity():
    file_name = "temp_conversion_tool.py"
    if not os.path.exists(file_name):
        print(f"Error: '{file_name}' does not exist.")
        return False
    elif os.path.getsize(file_name) == 0:
        print(f"Error: '{file_name}' is empty.")
        return False
    return True


# === GLOBAL CONVERSION FACTORS ===
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# === CONVERSION FUNCTIONS ===


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# === MAIN USER INTERACTION ===


def main():
    if not check_file_validity():
        return

    # Ask for temperature input
    temp_input = input("Enter the temperature to convert: ").strip()

    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Ask for unit input
    unit = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# === RUN PROGRAM ===
if __name__ == "__main__":
    main()

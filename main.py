import sys

def convert(value, from_unit, to_unit):
    # Supported conversions:
    # Length
    if from_unit == "m" and to_unit == "cm":
        return value * 100  # Convert meters to centimeters
    elif from_unit == "cm" and to_unit == "m":
        return value / 100  # Convert centimeters to meters
    elif from_unit == "km" and to_unit == "miles":
        return value * 0.621371  # Convert kilometers to miles
    elif from_unit == "miles" and to_unit == "km":
        return value / 0.621371  # Convert miles to kilometers
    # Velocity
    elif from_unit == "km/h" and to_unit == "m/s":
        return value * 0.277778  # Convert kilometers per hour to meters per second
    elif from_unit == "m/s" and to_unit == "km/h":
        return value * 3.6  # Convert meters per second to kilometers per hour
    elif from_unit == "km/h" and to_unit == "knots":
        return value * 0.539957  # Convert kilometers per hour to knots
    elif from_unit == "knots" and to_unit == "km/h":
        return value / 0.539957  # Convert knots to kilometers per hour
    # Mass
    elif from_unit == "kg" and to_unit == "lb":
        return value * 2.20462  # Convert kilograms to pounds
    elif from_unit == "lb" and to_unit == "kg":
        return value / 2.20462  # Convert pounds to kilograms
    # Volume
    elif from_unit == "liters" and to_unit == "cubic cm":
        return value * 1000  # Convert liters to cubic centimeters
    elif from_unit == "cubic cm" and to_unit == "liters":
        return value / 1000  # Convert cubic centimeters to liters
    # Power
    elif from_unit == "hp" and to_unit == "kw":
        return value * 0.7457  # Convert horsepower to kilowatts
    elif from_unit == "kw" and to_unit == "hp":
        return value / 0.7457  # Convert kilowatts to horsepower
    # Time
    elif from_unit == "hours" and to_unit == "minutes":
        return value * 60  # Convert hours to minutes
    elif from_unit == "minutes" and to_unit == "hours":
        return value / 60  # Convert minutes to hours
    # Other conversions...
    else:
        print("Unsupported conversion: {} to {}".format(from_unit, to_unit))
        sys.exit(1)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <value> <from_unit> <to_unit>".format(sys.argv[0]))
        sys.exit(1)

    try:
        value = float(sys.argv[1])  # Convert the first argument to a float value
    except ValueError:
        print("Invalid value: {}".format(sys.argv[1]))  # Handle invalid input value
        sys.exit(1)

    from_unit = sys.argv[2]  # Get the source unit from the second argument
    to_unit = sys.argv[3]    # Get the target unit from the third argument

    # Perform the conversion and print the result
    result = convert(value, from_unit, to_unit)
    print("{:.2f} {} = {:.5f} {}".format(value, from_unit, result, to_unit))

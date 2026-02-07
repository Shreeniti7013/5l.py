def length_converter(value, unit_in, unit_out):
    """
    Converts a length value from one unit to another.
    
    Supported units: mm, cm, m, km, inch, ft, mile.
    Base unit for calculation is meters (m).
    """
    # Conversion factors to meters (m)
    factors = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'inch': 0.0254, # 1 inch = 0.0254 meters
        'ft': 0.3048,  # 1 foot = 0.3048 meters
        'mile': 1609.34 # 1 mile = 1609.34 meters
    }

    if unit_in not in factors or unit_out not in factors:
        return "Error: Invalid unit. Use one of mm, cm, m, km, inch, ft, mile."
    
    # Convert input value to the base unit (meters)
    value_meters = value * factors[unit_in]
    
    # Convert from meters to the desired output unit
    converted_value = value_meters / factors[unit_out]
    
    return converted_value

# --- Example Usage ---
# Convert 10 kilometers to miles
km_value = 10
miles_value = length_converter(km_value, 'km', 'mile')
print(f"{km_value} kilometers is equal to {miles_value:.2f} miles") # Output: 10 kilometers is equal to 6.21 miles

# Convert 5 feet to meters
feet_value = 5
meters_value = length_converter(feet_value, 'ft', 'm')
print(f"{feet_value} feet is equal to {meters_value:.2f} meters") # Output: 5 feet is equal to 1.52 meters

# Convert 100 centimeters to inches
cm_value = 100
inches_value = length_converter(cm_value, 'cm', 'inch')
print(f"{cm_value} centimeters is equal to {inches_value:.2f} inches") # Output: 100 centimeters is equal to 39.37 inches

# Example with an invalid unit
invalid_result = length_converter(10, 'kg', 'm')
print(invalid_result)
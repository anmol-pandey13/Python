# Temperature Converter

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"Celsius: {celsius}°C")
print(f"Fahrenheit: {fahrenheit}°F")
print(f"Kelvin: {kelvin} K")
unit = input("Enter the unit of temperature (C or F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp_fahrenheit = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp_fahrenheit}°F")
elif unit == "F":
    temp_celsius = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp_celsius}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
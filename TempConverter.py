# Written by Christian Simmons
# Temperature Converter

print("=== Temperature Converter ===\n")

def convert_temp():
    #This function handles one temperature conversion.
    conversion_type = input("Type 'C' to convert C to F, or 'F' to convert F to C: ").upper().strip()

    # Celcius converter
    if conversion_type == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        
        print(f"\nRough Reading:     [{int(celsius)}°C  |  {int(fahrenheit)}°F]")
        print(f"Accurate Reading:  [{celsius:.2f}°C  |  {fahrenheit:.2f}°F]\n")

    # Fahrenheit converter
    elif conversion_type == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        
        print(f"\nRough Reading:     [{int(fahrenheit)}°F  |  {int(celsius)}°C]")
        print(f"Accurate Reading:  [{fahrenheit:.2f}°F  |  {celsius:.2f}°C]\n")
    
    # Safenet
    else:
        print("[ERROR!] Please type only 'C' or 'F'.\n")


# ==================== Call the function ====================
convert_temp()
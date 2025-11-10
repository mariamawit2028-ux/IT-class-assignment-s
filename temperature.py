def temperature_converter():
    conversion_type = input("Enter the conversion type ('C2F' for Celsius to Fahrenheit, 'F2C' for Fahrenheit to Celsius): ")
    value = float(input("Enter the temperature to convert: "))
    
    if conversion_type == 'C2F':
        result = (value * 9/5) + 32
        print(f"{value}ºC = {round(result, 2)}ºF")
    elif conversion_type == 'F2C':
        result = (value - 32) * 5/9
        print(f"{value}ºF = {round(result, 2)}ºC")
    else:
        print("Invalid conversion type.  Enter 'C2F' or 'F2C'.")
def length_converter():
    conversion_type = input(" Please enter the conversion type ('m2f' for meter to feet, 'f2m' for feet to meter): ")        
    value = float(input("enter the length to convert: "))
    if conversion_type == 'm2f':
        result = (value * 0.3048 )
        print(f"{value}m = {round(result, 2)}f")
    elif conversion_type == 'f2m':
        result = (value % 0.3048 )
        print(f"{value}f = {round(result, 2)}m")
print("press 1 for temprature")
print("press 2 for length")
choose = int(input())
if choose==1:
    temperature_converter()
elif choose==2:
    length_converter(),

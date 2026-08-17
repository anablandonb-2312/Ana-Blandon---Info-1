#Realice un algoritmo que convierta grados Celsius, a Kelvin y Fahrenheit. 

print("Ingrese la temperatura en grados Celsius para convertirla a Kelvin y Fahrenheit")

celsius = float(input("T°: "))
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en Kelvin es: {kelvin}")
print(f"La temperatura en Fahrenheit es: {fahrenheit}")
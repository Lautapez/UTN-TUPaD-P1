#Ejercicio 1

print ("Hola mundo")

#Ejercicio 2

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}")

#Ejercicio 3

nombre = input("Ingrese tu nombre: ")
apellido = input("Ingrese su apellido: ") 
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4

import math

radio = float(input("Ingrese el radio del círculo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#Ejercicio 5

segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos // 3600
segundos_restantes = segundos % 3600

print(f"{segundos} segundos equivalen a {horas} horas y {segundos_restantes} segundos.")

#Ejercicio 6

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7

numero1 = int(input("Introduzca el primer número que sea distinto de 0: "))
while numero1 == 0:
    numero1 = int(input("El número no puede ser 0, introduzca otro número: "))

numero2 = int(input("Introduzca el segundo número que sea distinto de 0: "))
while numero2 == 0:
    numero2 = int(input("El número no puede ser 0, introduzca otro número: "))

# Realizamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
# Para la división, verificamos que el segundo número no sea 0 (aunque ya lo comprobamos antes)
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Indefinido (división por 0)"

# Mostramos los resultados
print(f"\nResultados de las operaciones con los números {numero1} y {numero2}:")
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")

#Ejercicio 8

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

#Ejercicio 9

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

#Ejercicio 10

numero1 = float(input("Introduzca el primer número: "))
numero2 = float(input("Introduzca el segundo número: "))
numero3 = float(input("Introduzca el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los números {numero1}, {numero2} y {numero3} es: {promedio}")




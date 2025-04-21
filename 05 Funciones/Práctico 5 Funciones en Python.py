#Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

if __name__ == "__main__":
    imprimir_hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

if __name__ == "__main__":
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("¿Dónde vives?: ")

    informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5

def segundos_a_horas(segundos):
    horas = segundos // 3600 
    return horas

segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas.")

#Ejercicio 6

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)

#Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultado = operaciones_basicas(a, b)

print("\nResultados de las operaciones:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")

#Ejercicio 8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#Ejercicio 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

#Ejercicio 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio:.2f}")





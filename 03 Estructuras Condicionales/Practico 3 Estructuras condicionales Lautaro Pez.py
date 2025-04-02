#Ejercicio 1

edad = int(input("¿Cuántos años tienes? "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Ejercicio 2

nota = int(input("Ingrese su nota"))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3

numero = int(input("Por favor, ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4

edad = int(input("¿Cuántos años tienes? "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5

contraseña = input("Por favor, ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

import random
import statistics

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

print(f"Lista de números: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Tipo de sesgo: {sesgo}")

#Ejercicio 7

cadena = input("Ingresa una palabra o frase: ")

if cadena[-1].lower() in 'aeiou':
    # Si termina con vocal, añadir un signo de exclamación
    cadena += '!'
    
print(cadena)

#Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra mayúscula")

opcion = int(input("Ingrese el número de la opción que desee (1, 2 o 3): "))

if opcion == 1:
    resultado = nombre.upper()  
elif opcion == 2:
    resultado = nombre.lower()  
elif opcion == 3:
    resultado = nombre.title()  
else:
    resultado = "Opción no valida."

print("Resultado:", resultado)

#Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"

print(f"La magnitud {magnitud} se clasifica como: {clasificacion}")

#Ejercicio 10

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Introduce el número del mes actual (1-12): "))
dia = int(input("Introduce el día del mes actual: "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes < 3 or (mes == 3 and dia <= 20))):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes < 6 or (mes == 6 and dia <= 20))):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes < 9 or (mes == 9 and dia <= 20))):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (10 <= mes <= 12 and (mes < 12 or (mes == 12 and dia <= 20))):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    estacion = estacion_norte
elif hemisferio == "S":
    estacion = estacion_sur
else:
    estacion = "Hemisferio no válido"

print(f"Según la fecha y el hemisferio dados, la estación del año en que se encuentra es {estacion}")



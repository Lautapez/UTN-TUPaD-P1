#Ejercicio 1

for i in range(101):
    print(i)

#Ejercicio 2

def contar_digitos():
    try:
        numero = int(input("Ingrese un numero entero: "))
        cantidad_digitos = len(str(abs(numero)))
        print(f"El numero tiene {cantidad_digitos} digito(s).")
    except ValueError:
        print("Debe de ingresar un numero entero que sea valido.")

contar_digitos()

# Ejercicio 3

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

suma = sum(range(valor1 + 1, valor2))

print(f"La suma de los números que se encuentran entre {valor1} y {valor2} es de {suma}")

#Ejercicio 4

total = 0

while True:
    numero = int(input("Ingrese un numero que sea entero. Para deternerse ingrese el numero 0: "))
    
    if numero == 0:
        break
    
    total += numero

print(f"El total acumulado es: {total}")

#Ejercicio 5

import random

numero_para_adivinar = random.randint(0, 9)

intentos = 0

while True:
    adivinanza = int(input("Adivine un numero entre el 0 y 9: "))
    
    intentos += 1
    
    if adivinanza == numero_para_adivinar:
        print(f"Usted ha adivinado el numero en {intentos} intentos.")
        break
    elif adivinanza < numero_para_adivinar:
        print("El numero es mayor. Intenta de nuevo.")
    else:
        print("El numero es menor. Intenta de nuevo.")

#Ejercicio 6

for num in range(100, -1, -2):
    print(num)

#Ejercicio 7

numero = int(input("Ingrese un numero entero positivo: "))

if numero < 0:
    print("Debe de ingresar un numero entero positivo.")
else:
    suma = sum(range(1, numero + 1))
    
    print(f"La suma de los numeros entre 0 y {numero} es: {suma}")

#Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    numero = int(input(f"Ingrese el numero {i + 1} de los 100: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")

#Ejercicio 9

suma = 0
cantidad = 100

for i in range(cantidad):
    numero = int(input(f"Ingrese el numero {i + 1} de {cantidad}: "))
    suma += numero  

media = suma / cantidad

print(f"La media de los {cantidad} numeros ingresados es: {media}")

#Ejercicio 10

def invertir_digitos():
    try:
        numero = int(input("Ingrese un numero entero: "))
        signo = -1 if numero < 0 else 1
        numero_invertido = int(str(abs(numero))[::-1]) * signo
        print(f"El numero invertido quedara asi: {numero_invertido}")
    except ValueError:
        print("Debe de ingresar un numero entero que sea valido.")

invertir_digitos()


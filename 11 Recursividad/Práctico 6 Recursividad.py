#Ejercicio 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    numero = int(input("Introduzca un numero entero mayor que 0: "))
    if numero < 1:
        print("El numero tiene que ser mayor que 0.")
    else:
        for i in range(1, numero + 1):
            print(f"Factorial de {i} es {factorial(i)}")
except ValueError:
    print("Debe de introducir un numero que sea valido.")

#Ejercicio 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    posicion = int(input("Introduzca una posicion (Debe ser un entero mayor o igual a 0): "))
    if posicion < 0:
        print("La posicion debe ser 0 o mayor.")
    else:
        print("Serie de Fibonacci:")
        for i in range(posicion + 1):
            print(f"F({i}) = {fibonacci(i)}")
except ValueError:
    print("Tiene que introducir un numero entero que sea valido.")

#Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

try:
    base = float(input("Introduzca la base: "))
    exponente = int(input("Introduzca el exponente que sea un entero no negativo: "))

    if exponente < 0:
        print("El exponente debe ser un entero no negativo.")
    else:
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
except ValueError:
    print("Entrada invalida.")

#Ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return ""  
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  
try:
    numero = int(input("Introduzca un numero entero positivo: "))
    
    if numero < 0:
        print("Introduzca un numero entero positivo.")
    elif numero == 0:
        print("La representacion binaria de 0 es 0.")
    else:
        binario = decimal_a_binario(numero)
        print(f"La representación binaria de {numero} es {binario}")
except ValueError:
    print("Entrada invalida.")

#Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

try:
    palabra = input("Introduzca una palabra que no tenga espacios ni tildes: ").lower()
    
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palindromo.")
    else:
        print(f"La palabra '{palabra}' no es un palindromo.")
except ValueError:
    print("Entrada invalida.")

#Ejercicio 6

def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

try:
    numero = int(input("Introduzca un numero entero positivo: "))
    
    if numero < 0:
        print("Debe de introducir un numero entero positivo.")
    else:
        resultado = suma_digitos(numero)
        print(f"La suma de los digitos de {numero} es {resultado}.")
except ValueError:
    print("Entrada invalida.")

#Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

#Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)  # Sumar 1 y llamar recursivamente
    else:
        return contar_digito(numero // 10, digito)  # Llamada recursiva sin contar

try:
    numero = int(input("Introduzca un número entero positivo: "))
    digito = int(input("Introduzca el digito que desee contar entre 0 y 9: "))
    
    if numero < 0 or digito < 0 or digito > 9:
        print("Tiene que introducir un numero entero positivo y un dígito entre 0 y 9.")
    else:
        resultado = contar_digito(numero, digito)
        print(f"El digito {digito} aparece {resultado} veces en el numero {numero}.")
except ValueError:
    print("Entrada invalida.")

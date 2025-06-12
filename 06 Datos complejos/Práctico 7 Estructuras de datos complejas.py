# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2

precios_frutas = {
    'Banana': 1200, 
    'Anana': 2500, 
    'Melon': 3000, 
    'Uva': 1450, 
    'Naranja': 1200, 
    'Manzana': 1500, 
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

#Ejercicio 3

precios_frutas = {
    'Banana': 1330, 
    'Anana': 2500, 
    'Melon': 2800, 
    'Uva': 1450, 
    'Naranja': 1200, 
    'Manzana': 1700, 
    'Pera': 2300
}

frutas = list(precios_frutas.keys())

print(frutas)

#Ejercicio 4

contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el numero de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingrese el nombre del contacto que quiera buscar: ")

if consulta in contactos:
    print(f"El numero de {consulta} es {contactos[consulta]}")
else:
    print(f"No se encontro ningun contacto con el nombre '{consulta}'.")

#Ejercicio 5

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Palabras unicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

#Ejercicio 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")

#Ejercicio 7

parcial_1 = {'Facundo', 'Luis', 'Pedro', 'Maria', 'Carlos'}
parcial_2 = {'Luis', 'Pedro', 'Juan', 'Maria', 'Elena'}

aprobaron_ambos = parcial_1 & parcial_2
print("Estudiantes que aprobaron ambos parciales:", aprobaron_ambos)

aprobaron_solo_uno = parcial_1 ^ parcial_2
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobaron_solo_uno)

aprobaron_al_menos_uno = parcial_1 | parcial_2
print("Estudiantes que aprobaron al menos un parcial:", aprobaron_al_menos_uno)

#Ejercicio 8

stock = {
    "manzanas": 50,
    "naranjas": 30,
    "bananas": 20
}

def consultar_stock():
    producto = input("Ingrese el nombre del producto para consultar el stock: ").lower()
    if producto in stock:
        print(f"El stock de {producto} es: {stock[producto]} unidades.")
    else:
        print(f"El producto {producto} no existe en el inventario.")

def agregar_stock():
    producto = input("Ingrese el nombre del producto para agregar unidades: ").lower()
    if producto in stock:
        cantidad = int(input(f"¿Cuántas unidades de {producto} deseas agregar? "))
        stock[producto] += cantidad
        print(f"Se han agregado {cantidad} unidades de {producto}. El stock actualizado es: {stock[producto]}.")
    else:
        print(f"El producto {producto} no existe en el inventario.")

def agregar_producto():
    producto = input("Ingrese el nombre del nuevo producto: ").lower()
    if producto in stock:
        print(f"El producto {producto} ya existe en el inventario.")
    else:
        cantidad = int(input(f"¿Cuantas unidades de {producto} quiere agregar? "))
        stock[producto] = cantidad
        print(f"El producto {producto} ha sido agregado con {cantidad} unidades al inventario.")

def menu():
    while True:
        print("\n Menú de opciones ")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            consultar_stock()
        elif opcion == "2":
            agregar_stock()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            print("Adios")
            break
        else:
            print("Opción no invalida. Intente de nuevo.")

menu()

#Ejercicio 9

agenda = {}

def mostrar_menu():
    print("\n--- AGENDA ---")
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Eliminar evento")
    print("4. Ver agenda completa")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elija una opcion del 1 al 5: ")

    if opcion == "1":
        dia = input("Dia: ").lower()
        hora = input("Hora (Formato de 24 HS por ejemplo 14:00): ")
        evento = input("Descripcion del evento: ")
        agenda[(dia, hora)] = evento
        print("Evento agregado correctamente.")

    elif opcion == "2":
        dia = input("Dia: ").lower()
        hora = input("Hora (Formato de 24 HS por ejemplo 14:00): ")
        evento = agenda.get((dia, hora), "No hay actividades programadas.")
        print(f"Evento: {evento}")

    elif opcion == "3":
        dia = input("Dia: ").lower()
        hora = input("Hora (Formato de 24 HS por ejemplo 14:00): ")
        if (dia, hora) in agenda:
            del agenda[(dia, hora)]
            print("Evento eliminado.")
        else:
            print("No se encontro ningun evento en ese dia y hora.")

    elif opcion == "4":
        if agenda:
            print("\nAgenda completa:")
            for clave in sorted(agenda):
                print(f"{clave[0].capitalize()} a las {clave[1]}: {agenda[clave]}")
        else:
            print("La agenda esta vacia.")

    elif opcion == "5":
        print("Adios")
        break

    else:
        print("Opcion invalida. Debe elegir una opcion del 1 al 5.")

#Ejercicio 10

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)

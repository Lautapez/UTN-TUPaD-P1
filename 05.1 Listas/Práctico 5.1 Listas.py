#Ejercicio 1

multiplos_4 = [x for x in range(1, 101) if x % 4 == 0]
print(multiplos_4)

#Ejercicio 2

F2004=1
W11=2
RB7=3
BGP001=4
FW14=5
mi_lista = [F2004, W11, RB7, BGP001, FW14]

print("El penúltimo elemento de esta lista es:", mi_lista[-2])

#Ejercicio 3

palabras = []

palabras.append("Chasis")
palabras.append("Carbono")
palabras.append("Suspension")

print("Lista resultante:", palabras)

#Ejercicio 4

lista_animales = []

lista_animales.append("Chasis")
lista_animales.append("Loro")
lista_animales.append("Oso")

print("Lista resultante:", lista_animales)

#Ejercicio 5

#Se crea una lista llamada numeros con los valores [8, 15, 3, 22, 7], luego se identifica el valor máximo de la lista usando max(numeros), que es el numero 22. Despues se elimina el numero máximo de la lista usando numeros.remove(max(numeros)), eliminando en el proceso el numero 22. Por ultimo se imprime la lista actualizada, que es [8, 15, 3, 7].

#Ejercicio 6

numeros = list(range(10, 31, 5))

print(numeros[:2])

#Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["aventador", "C63"]

print(autos)

#Ejercicio 8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][compras[1].index("fideos")] = "tallarines"

compras[0].remove("pan")

print(compras)

#Ejercicio 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

